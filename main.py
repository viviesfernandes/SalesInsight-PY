
import os
import modulo_vendas as mv


def main():
    print("=" * 60)
    print(" SALESINSIGHT PY - PIPELINE DE VENDAS")
    print("=" * 60)

    arquivo_dados = "vendas.csv"

    # 1. Gerar dataset sintetico se nao existir
    if not os.path.exists(arquivo_dados):
        mv.gerar_dataset_sintetico(
            arquivo_dados,
            n_registros=150
        )

    # 2. Leitura dos dados
    dados_brutos = mv.carregar_csv(arquivo_dados)

    # 3. Inspecao inicial
    mv.inspecionar_dados(dados_brutos)

    # 4. Limpeza e tratamento
    dados_limpos = mv.limpar_dados(dados_brutos)

    # 5. Criacao dos campos derivados
    dados_transformados = mv.criar_campos_derivados(
        dados_limpos
    )

    # 6. Transformacao utilizando lambda
    dados_com_tag = mv.processar_transformacao(
        dados_transformados,
        lambda item: {
            **item,
            "processado": True
        }
    )

    # 7. Calculo das metricas agregadas
    metricas = mv.calcular_metricas(
        dados_com_tag
    )

    # 8. Segmentacao dos clientes
    segmentos = mv.segmentar_clientes(
        dados_com_tag
    )

    # 9. Obtencao dos principais clientes
    top_clientes = mv.obter_top_clientes(
        segmentos,
        top_n=5
    )

    # 10. Exibicao dos resultados
    print("\n" + "=" * 60)
    print(" RESUMO EXECUTIVO")
    print("=" * 60)

    print(
        f"Receita total da empresa: "
        f"R$ {metricas['total_geral']:.2f}"
    )

    print("\nReceita por categoria:")

    for categoria, receita in metricas["por_categoria"].items():
        print(
            f" - {categoria}: R$ {receita:.2f}"
        )

    print("\nReceita por regiao:")

    for regiao, receita in metricas["por_regiao"].items():
        print(
            f" - {regiao}: R$ {receita:.2f}"
        )

    print("\nTop 5 clientes:")

    for cliente, info in top_clientes:
        print(
            f" - {cliente}: "
            f"R$ {info['total_gasto']:.2f} "
            f"| Segmento: {info['segmento']}"
        )

    # 11. Exportacao dos resultados
    mv.exportar_resultados(
        metricas,
        segmentos,
        pasta_saida="outputs"
    )

    print("\n" + "=" * 60)
    print("[CONCLUIDO] Pipeline executado com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    main()
