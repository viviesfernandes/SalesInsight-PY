# SalesInsight PY - Pipeline de Análise de Dados de Vendas

Projeto desenvolvido em Python para tratamento, transformação e análise de dados de vendas.

O SalesInsight PY utiliza recursos nativos da linguagem Python para gerar métricas de vendas, segmentar clientes e exportar relatórios em arquivos CSV e JSON.

## 📁 Estrutura do Projeto

- `main.py`: Arquivo principal responsável pela execução do pipeline.
- `modulo_vendas.py`: Módulo contendo as funções de geração, leitura, limpeza, transformação e análise dos dados.
- `vendas.csv`: Dataset de vendas utilizado como entrada.
- `outputs/`: Diretório contendo os relatórios gerados.
- `outputs/estatisticas.json`: Arquivo com as métricas gerais e a segmentação dos clientes.
- `outputs/metricas_resumo.csv`: Arquivo com o resumo das receitas por categoria.

## 🚀 Como Executar

### Requisitos

- Python 3 instalado.
- Visual Studio Code ou outro editor de código.
- Terminal aberto na pasta do projeto.

### Execução

1. Abra a pasta `SalesInsight PY` no Visual Studio Code.
2. Abra o terminal integrado.
3. Execute o seguinte comando:

```bash
python main.py
```

4. Aguarde o processamento dos dados.
5. Confira os resultados exibidos no terminal e os arquivos gerados na pasta `outputs/`.

## ⚙️ Funcionalidades

- Geração de dataset sintético de vendas.
- Leitura de arquivos CSV utilizando o módulo `csv`.
- Inspeção inicial dos dados.
- Limpeza e tratamento de dados inconsistentes.
- Conversão de tipos de dados.
- Criação de campos derivados, como receita total e faixa de preço.
- Cálculo de métricas agregadas por categoria e região.
- Segmentação de clientes por faixa de gasto acumulado.
- Identificação dos principais clientes.
- Exportação de resultados em CSV e JSON.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Biblioteca padrão `csv`
- Biblioteca padrão `json`
- Biblioteca padrão `random`
- Biblioteca padrão `os`
- Git para versionamento do projeto

## 📊 Resultados

O projeto gera relatórios contendo:

- Receita total das vendas.
- Receita por categoria.
- Receita por região.
- Segmentação dos clientes.
- Principais clientes por gasto acumulado.

Os resultados são armazenados na pasta `outputs/`.

## 👨‍💻 Autor

Projeto desenvolvido como mini-projeto avaliativo do Módulo 01.
