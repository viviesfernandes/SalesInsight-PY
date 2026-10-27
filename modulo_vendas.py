
import csv
import random
import json
import os


# RF01 - Gerar dataset sintetico
def gerar_dataset_sintetico(
    caminho_arquivo="vendas.csv",
    n_registros=100,
    seed=42
):
    random.seed(seed)

    produtos = [
        "Notebook",
        "Smartphone",
        "Tablet",
        "Monitor",
        "Teclado",
        "Mouse"
    ]

    categorias = {
        "Notebook": "Eletrônicos",
        "Smartphone": "Celulares",
        "Tablet": "Celulares",
        "Monitor": "Eletrônicos",
        "Teclado": "Acessórios",
        "Mouse": "Acessórios"
    }

    regioes = [
        "Sudeste",
        "Sul",
        "Nordeste",
        "Centro-Oeste",
        "Norte"
    ]

    cabecalho = [
        "id_venda",
        "data_venda",
        "cliente",
        "produto",
        "categoria",
        "regiao",
        "quantidade",
        "preco_unitario"
    ]

    dados = []

    for i in range(1, n_registros + 1):
        prod = random.choice(produtos)

        qtd = (
            str(random.randint(1, 8))
            if random.random() > 0.05
            else ""
        )

        preco = (
            str(round(random.uniform(100, 3500), 2))
            if random.random() > 0.05
            else ""
        )

        prod_nome = (
            f"     {prod} "
            if random.random() < 0.1
            else prod
        )

        dados.append([
            i,
            f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            f"Cliente_{random.randint(1, 30):03d}",
            prod_nome,
            categorias.get(prod, "Outros"),
            random.choice(regioes),
            qtd,
            preco
        ])

    with open(
        caminho_arquivo,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(cabecalho)
        writer.writerows(dados)

    print(f"[OK] Dataset gerado em: {caminho_arquivo}")


# RF07 - Carregar CSV
def carregar_csv(caminho_arquivo):
    dados = []

    with open(
        caminho_arquivo,
        mode="r",
        encoding="utf-8"
    ) as f:

        leitor = csv.DictReader(f)

        for linha in leitor:
            dados.append(linha)

    return dados


# RF02 - Inspecionar dados
def inspecionar_dados(dados):
    print("\n=== INSPEÇÃO INICIAL DOS DADOS ===")
    print(f"Total de registros carregados: {len(dados)}")

    if not dados:
        print("Nenhum registro foi encontrado.")
        return

    print(f"Campos disponíveis: {list(dados[0].keys())}")
    print(f"Exemplo do primeiro registro: {dados[0]}")

    incompletos = []

    for numero, linha in enumerate(dados, start=1):
        campos_vazios = [
            campo
            for campo, valor in linha.items()
            if valor is None or str(valor).strip() == ""
        ]

        if campos_vazios:
            incompletos.append((numero, campos_vazios))

    print(
        f"Registros incompletos ou com valores nulos: "
        f"{len(incompletos)}"
    )

    for numero, campos in incompletos:
        print(
            f" - Registro {numero}: campos vazios: "
            f"{', '.join(campos)}"
        )

# RF03 - Limpar e tratar dados
def limpar_dados(dados_brutos):
    dados_limpos = []
    removidos = 0

    for lin in dados_brutos:

        # Tratamento de espaços
        prod = lin["produto"].strip().title()
        cat = lin["categoria"].strip().title()
        reg = lin["regiao"].strip().title()
        cli = lin["cliente"].strip()

        # Validacao de nulos/vazios
        if (not prod or not cat or not reg or not cli
                or not lin["quantidade"].strip()
                or not lin["preco_unitario"].strip()):
            removidos += 1
            continue

        try:
            qtd = int(lin["quantidade"])
            preco = float(lin["preco_unitario"])

            dados_limpos.append({
                "id_venda": int(lin["id_venda"]),
                "data_venda": lin["data_venda"].strip(),
                "cliente": cli,
                "produto": prod,
                "categoria": cat,
                "regiao": reg,
                "quantidade": qtd,
                "preco_unitario": preco
            })

        except ValueError:
            removidos += 1

    print("\n=== RELATÓRIO DE LIMPEZA ===")

    print(
        f"Registros Válidos: {len(dados_limpos)} | "
        f"Registros Removidos: {removidos}"
    )

    return dados_limpos


# RF04 - Criar campos derivados
def criar_campos_derivados(dados):
    for item in dados:

        receita = round(
            item["quantidade"] * item["preco_unitario"],
            2
        )

        item["receita_total"] = receita

        if receita < 500:
            item["faixa_preco"] = "Baixo"

        elif receita <= 2000:
            item["faixa_preco"] = "Médio"

        else:
            item["faixa_preco"] = "Alto"

    return dados


# RF05 - Calcular métricas agregadas
def calcular_metricas(dados):
    receita_categoria = {}
    receita_regiao = {}
    total_geral = 0.0

    for item in dados:

        cat = item["categoria"]
        reg = item["regiao"]
        rec = item["receita_total"]

        receita_categoria[cat] = round(
            receita_categoria.get(cat, 0.0) + rec,
            2
        )

        receita_regiao[reg] = round(
            receita_regiao.get(reg, 0.0) + rec,
            2
        )

        total_geral += rec

    return {
        "total_geral": round(total_geral, 2),
        "por_categoria": receita_categoria,
        "por_regiao": receita_regiao
    }


# RF06 - Segmentar clientes
def segmentar_clientes(dados):
    gastos_cliente = {}

    for item in dados:

        cli = item["cliente"]

        gastos_cliente[cli] = (
            gastos_cliente.get(cli, 0.0)
            + item["receita_total"]
        )

    segmentos = {}

    for cli, total in gastos_cliente.items():

        if total > 8000:
            cat = "Ouro"

        elif total >= 3000:
            cat = "Prata"

        else:
            cat = "Bronze"

        segmentos[cli] = {
            "total_gasto": round(total, 2),
            "segmento": cat
        }

    return segmentos


# RF07 - Exportar resultados
def exportar_resultados(
    metricas,
    clientes,
    pasta_saida="outputs"
):
    os.makedirs(pasta_saida, exist_ok=True)

    # Exportar JSON
    caminho_json = os.path.join(
        pasta_saida,
        "estatisticas.json"
    )

    with open(
        caminho_json,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "metricas_gerais": metricas,
                "clientes": clientes
            },
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"[OK] Arquivo JSON exportado em: {caminho_json}")

    # Exportar CSV
    caminho_csv = os.path.join(
        pasta_saida,
        "metricas_resumo.csv"
    )

    with open(
        caminho_csv,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        escritor = csv.writer(f)

        escritor.writerow([
            "Categoria",
            "Receita Total"
        ])

        for cat, rec in metricas["por_categoria"].items():
            escritor.writerow([cat, rec])

    print(f"[OK] Arquivo CSV exportado em: {caminho_csv}")


# Função de transformação com lambda
def processar_transformacao(dados, funcao):
    return [
        funcao(item)
        for item in dados
    ]


# Obter os principais clientes
def obter_top_clientes(segmentos, top_n=5):
    clientes_ordenados = sorted(
        segmentos.items(),
        key=lambda item: item[1]["total_gasto"],
        reverse=True
    )

    return clientes_ordenados[:top_n]
