# ProjetoAvaliativo-Modulo1
Projeto Avaliativo do Módulo 1 - Modelagem de dados da SCTEC.
Produzido por Lorena Daumann, turma V3 - Ciclo 2 - Vizualização de dados e Business Intelligence.

---
O objetivo do trabalho é atuar como analista de dados para extrair, analisar e visualizar dados de Recursos Humanos do banco FreeSQL, transformando dados brutos em insights que apoiem decisões estratégicas sobre a distribuição salarial por cargo/departamento e a dispersão geográfica dos funcionários. Este projeto analisa dados de Recursos Humanos do schema HR, relacionando funcionários, salários, departamentos, cargos e localização geográfica.

A proposta é partir das consultas SQL, exportar os resultados em CSV e usar Python para transformar esses dados em estatísticas e visualizações. A análise busca responder: como os salários estão distribuídos, quais departamentos concentram mais funcionários, quais cargos têm maiores médias salariais e como a distribuição geográfica influencia a leitura dos resultados

---
## Objetivos
- Extrair dados de RH com consultas SQL usando LEFT JOIN.
- Gerar arquivos CSV a partir dos resultados das consultas.
- Explorar os dados em Python com pandas, matplotlib e seaborn.
- Calcular média, mediana, mínimo e máximo dos salários.
- Criar visualizações para apoiar a interpretação dos dados.
- Apresentar os principais insights encontrados na análise.

---
## Estrutura do Repositório

```text
├── LICENSE                # Licença de código
├── Projeto.py             # Análise em Python
├── README.md              # Consultas SQL usadas na extração
├── query_01.csv           # Arquivos CSV exportados das consultas SQL
├── query_01.sql           # Consultas SQL usadas na extração
├── query_02.csv           # Arquivos CSV exportados das consultas SQL
└── query_02.sql           # Consultas SQL usadas na extração
```

---
O projeto utiliza <b>seis tabelas integradas</b> do esquema de Recursos Humanos (HR):
- <b>HR.EMPLOYEES:</b> Tabela central que armazena os dados cadastrais e financeiros de cada funcionário, como nome, salário e identificadores de cargo e departamento.
- <b>HR.JOBS:</b> Contém o catálogo de cargos disponíveis na organização, especificando os títulos profissionais e as faixas salariais permitidas (mínima e máxima).
- <b>HR.DEPARTMENTS:</b> Identifica as divisões internas da empresa (como TI, Finanças e Vendas) e faz o vínculo com a localidade onde operam.
- <b>HR.LOCATIONS:</b> Detalha os endereços físicos dos escritórios, incluindo dados de rua, CEP, cidade e o estado ou província correspondente.
- <b>HR.COUNTRIES:</b> Associa cada cidade a um país específico dentro do mapeamento corporativo.
- <b>HR.REGIONS:</b> Agrupa os países em grandes blocos geográficos ou continentes para análises de alto nível.

---
## Sobre as Consultas SQL
As consultas foram estruturadas para extrair e cruzar as informações operacionais e geográficas solicitadas pelo RH:
- Query 1 (Salários por Departamento e Cargo): Cruza os registros de funcionários com seus respectivos departamentos e cargos (LEFT JOIN entre EMPLOYEES, DEPARTMENTS e JOBS). Ela aplica um filtro para trazer apenas funcionários com salários ativos (WHERE SALARY > 0) e ordena os resultados alfabeticamente pelo primeiro nome.
- Query 2 (Funcionários por Região e Localização): Realiza o rastreamento geográfico completo dos colaboradores vinculando sucessivamente as tabelas de departamentos, cargos, localizações, países e regiões. O filtro descarta registros sem local definido (WHERE LOCATION_ID IS NOT NULL) e também entrega a listagem ordenada pelo nome dos profissionais.
<br>  
  
| Query | Arquivo gerado | Campos retornados | Filtro aplicado |
| --- | --- | --- | --- |
| `sql/query_1.sql` | `data/query_01.csv` | funcionário, nome, sobrenome, salário, departamento e cargo | salários maiores que zero |
| `sql/query_2.sql` | `data/query_02.csv` | funcionário, nome, sobrenome, salário, departamento, endereço, cidade, estado, país e região | registros com região informada |

A primeira consulta apoia a análise salarial por departamento e cargo. A segunda amplia a leitura dos dados ao incluir localização, país e região.

---
## Explicação da análise feita em Python;
Foi realizada uma Análise Exploratória de Dados (EDA) simples. 
Primeiro foi realizada a visualização inicial dos dados, mostrando aspectos como cabeçalho dos queries, informações de dataframe, estatísticas descritivas, total de duplicatas e a exclusão dessas mesmas.
<br> Para a Query 1, foram analisadas a quantidade de departamentos por localização, a vizualização de dados - nulos que pode significar que aqueles nos quais tem o MANAGER_ID nulo ainda não estão ativos efetivamente - e o agrupamento de departamentos de âmbito comum,ou seja, a concentração de departamentos por área de atuação.
<br> Para a Query 2, foram analisadas a média salarial dos cargos, a vizualização de piso salarial (valor mínimo) e o teto salarial (valor máximo)


---
## Principais resultados encontrados

A análise exploratória dos dados de Recursos Humanos revelou insights estratégicos sobre a estrutura organizacional e a remuneração da empresa:

* **Concentração de Departamentos por Área de Atuação:** Através da contagem de ocorrências por área de negócio (`value_counts()`), identificou-se quais setores concentram o maior volume de movimentações e departamentos ativos, permitindo ao RH visualizar com clareza o peso operacional de cada vertical de negócio.
* **Mapeamento de Cargos e Faixas Salariais:** O cruzamento de dados gerou uma visão consolidada de remuneração. Foi possível identificar não apenas a média salarial real praticada para cada título de cargo (`JOB_TITLE`), mas também confrontar esses valores diretamente com o piso (mínimo) e o teto (máximo) salariais estipulados na tabela de cargos.
* **Identificação de Inconsistências/Registros Nulos:** A análise de dados nulos apontou registros com `MANAGER_ID` ausente, o que sugeriu a existência de departamentos ou colaboradores ainda em fase de ativação ou reestruturação interna.
* **Distribuição Geográfica:** O rastreamento de ponta a ponta (vinculando funcionários desde suas cidades até suas respectivas macrorregiões) evidenciou como a dispersão geográfica influencia a leitura das médias salariais e onde estão alocados os principais polos de talentos da organização.

---

## Como executar o projeto

Siga as instruções abaixo para configurar o ambiente local e executar a análise de dados.

### Pré-requisitos
Antes de começar, você precisa ter instalado em sua máquina:
* **Python 3.x** (recomenda-se a versão utilizada no desenvolvimento ou superior)
* **Git** (para clonar o repositório)

### Instalação das Bibliotecas
Os dados extraídos do banco de dados FreeSQL são processados em Python utilizando bibliotecas analíticas e de visualização de dados. Instale-as executando o comando abaixo no seu terminal:

```bash
pip install pandas matplotlib seaborn
```

### Comandos Necessários para Execução

1. **Clone o repositório para o seu computador:**
   ```bash
   git clone https://github.com
   ```

2. **Navegue até a pasta do projeto:**
   ```bash
   cd ProjetoAvaliativo-Modulo1-Ciclo2
   ```

3. **Execute o script principal de análise:**
   ```bash
   python Projeto.py
   ```

*Nota: Certifique-se de manter os arquivos `query_01.csv` e `query_02.csv` na mesma raiz do arquivo `Projeto.py` (conforme a estrutura do repositório), pois o script fará a leitura local desses arquivos para gerar as estatísticas e salvar os gráficos automaticamente.*


---
## Imagens dos gráficos gerados para a visualização dos resultados:
<img width="1000" height="500" alt="bargrafic_concentracao_departamentos" src="https://github.com/user-attachments/assets/475227e7-3314-4ceb-b880-e2931c29f7f4" />
<img width="2001" height="1267" alt="heatmap_salario_medio" src="https://github.com/user-attachments/assets/7223cabf-ab86-4543-ba21-de236015a231" />
