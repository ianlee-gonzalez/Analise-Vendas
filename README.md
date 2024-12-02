# Análise de Vendas com Flask

Este é um projeto que permite a análise de vendas através do upload de arquivos CSV. O sistema calcula automaticamente a receita total e o lucro total, exibe os dados em uma interface web e permite o download de um arquivo atualizado com os cálculos.

## Funcionalidades

- **Upload de Arquivo CSV**: Permite que o usuário envie um arquivo com dados de vendas.
- **Cálculo Automático**:
  - Receita Total: Calculada com base na quantidade e no preço unitário.
  - Lucro Total: Calculado como a diferença entre a receita e o custo total.
- **Resumo por Categoria**: Exibe o total de vendas e lucros agrupados por categoria de produtos.
- **Download de Arquivo Atualizado**: Gera um novo arquivo CSV com colunas de Receita e Lucro adicionadas.

## Requisitos

- Python 3.8 ou superior
- As dependências estão listadas no arquivo `requirements.txt`:
  - Flask
  - Pandas
  - Matplotlib (se precisar de gráficos no futuro)

## Como Executar

1. Clone este repositório no seu computador:
   ```bash
   git clone https://github.com/ianlee-gonzalez/analise-vendas.git
   cd analise-vendas
## Estrutura do Arquivo CSV

O arquivo CSV enviado pelo usuário deve conter as seguintes colunas obrigatórias:

| **Coluna**         | **Descrição**                                         |
|---------------------|-------------------------------------------------------|
| **Data**           | Data da venda (formato livre).                        |
| **Produto**        | Nome ou descrição do produto.                         |
| **Categoria**      | Categoria do produto (ex.: Eletrônicos).              |
| **Quantidade**     | Quantidade de itens vendidos.                         |
| **Preco_Unitario** | Preço por unidade do produto.                         |
| **Custo_Unitario** | Custo por unidade do produto.                         |

### Colunas Adicionadas pelo Sistema

Após o upload do arquivo, o sistema calculará e adicionará automaticamente as seguintes colunas:

- **Receita_Total**: `Quantidade * Preco_Unitario`
- **Lucro_Total**: `Quantidade * (Preco_Unitario - Custo_Unitario)`   
