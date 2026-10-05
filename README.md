# ProjetoAvaliativo-Modulo1
Projeto Avaliativo do Módulo 1 - Modelagem de dados da SCTEC.
Produzido por Lorena Daumann, turma V3 - Ciclo 2 - Vizualização de dados e Business Intelligence.

O objetivo do trabalho é atuar como analista de dados para extrair, analisar e visualizar dados de Recursos Humanos do banco FreeSQL, transformando dados brutos em insights que apoiem decisões estratégicas sobre a distribuição salarial por cargo/departamento e a dispersão geográfica dos funcionários. 

---
## Explicação das Tabelas Usadas
O projeto utiliza seis tabelas integradas do esquema de Recursos Humanos (HR):
- HR.EMPLOYEES: Tabela central que armazena os dados cadastrais e financeiros de cada funcionário, como nome, salário e identificadores de cargo e departamento.
- HR.JOBS: Contém o catálogo de cargos disponíveis na organização, especificando os títulos profissionais e as faixas salariais permitidas (mínima e máxima).
- HR.DEPARTMENTS: Identifica as divisões internas da empresa (como TI, Finanças e Vendas) e faz o vínculo com a localidade onde operam.
- HR.LOCATIONS: Detalha os endereços físicos dos escritórios, incluindo dados de rua, CEP, cidade e o estado ou província correspondente.
- HR.COUNTRIES: Associa cada cidade a um país específico dentro do mapeamento corporativo.
- HR.REGIONS: Agrupa os países em grandes blocos geográficos ou continentes para análises de alto nível.

---
## Resumo das Consultas SQL
As consultas foram estruturadas para extrair e cruzar as informações operacionais e geográficas solicitadas pelo RH:
- Query 1 (Salários por Departamento e Cargo): Cruza os registros de funcionários com seus respectivos departamentos e cargos (LEFT JOIN entre EMPLOYEES, DEPARTMENTS e JOBS). Ela aplica um filtro para trazer apenas funcionários com salários ativos (WHERE SALARY > 0) e ordena os resultados alfabeticamente pelo primeiro nome.
- Query 2 (Funcionários por Região e Localização): Realiza o rastreamento geográfico completo dos colaboradores vinculando sucessivamente as tabelas de departamentos, cargos, localizações, países e regiões. O filtro descarta registros sem local definido (WHERE LOCATION_ID IS NOT NULL) e também entrega a listagem ordenada pelo nome dos profissionais.


---
## Explicação da análise feita em Python;

---
## Principais resultados encontrados;

---
## Como executar o projeto, incluindo os pré-requisitos, a instalação das bibliotecas e os comandos necessários.

---
## Sugestões de melhoria para futuras versões.

---
## Imagens dos gráficos gerados para a visualização dos resultados:
