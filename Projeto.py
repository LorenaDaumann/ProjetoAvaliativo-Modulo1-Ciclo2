import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("query_01.csv")
df2 = pd.read_csv("query_02.csv")


# Vizualização inicial do dados
print("Cabeçalho Query 1:")
print(df.head())
print("\nCabeçalho Query 2:")
print(df2.head())

print("\n\nInformações do dataframe do Query 1:")
print(df.info())
print("\nInformações do dataframe do Query 2:")
print(df2.info())

print("\n\n\nEstatísticas descritivas do Query 1:")
print(df.describe())
print("\nEstatísticas descritivas Query 2:")
print(df2.describe())


# Organização e limpeza dos dados
print("\n\n\nTotal de duplicatas da Query 1:")
print(df.duplicated())
print("\nTotal de duplicatas da Query 2:")
print(df2.duplicated())

# removendo duplicatas
df = df.drop_duplicates()
df2 = df2.drop_duplicates()



print("\n\n\nANÁLISE DE DADOS EXPLORATÓRIA")

print("ANÁLISE QUERY 1")
####### Por localização
print("Quantidade de departamentos que estão localizados em 1700:")
quantidade = (df["LOCATION_ID"] == 1700).sum()
print(quantidade)

print("Quantidade de departamentos que estão localizados acima de 2000:")
quantidade2 = (df["LOCATION_ID"] >= 2000).sum()
print(quantidade2)

print("Quantidade de departamentos que estão localizados acima de 2500:")
quantidade3 = (df["LOCATION_ID"] >= 2500).sum()
print(quantidade3)

######## Dados nulos
print("\nDados nulos: ", df.isnull().sum()) #aqueles que estão nulos pode ser que não estejam ativos ainda

######## Agrupamento de departamentos de âmbito comum 
#Início de auxilío da IA
# Função para mapear cada departamento para sua macroárea
def mapear_area(depto):
    depto = str(depto).strip() #converte a variável para texto e remove os espaços em branco inúteis do início e do fim dela para padronizar os dados
    
    if depto in ["IT", "IT Support", "NOC", "IT Helpdesk"]:
        return "Tecnologia da Informação"
    elif depto in ["Finance", "Accounting", "Treasury", "Corporate Tax", "Control And Credit", "Shareholder Services", "Payroll"]:
        return "Finanças e Contabilidade"
    elif depto in ["Marketing", "Public Relations", "Sales", "Government Sales", "Retail Sales"]:
        return "Vendas e Marketing"
    elif depto in ["Human Resources", "Benefits", "Recruiting"]:
        return "Recursos Humanos"
    elif depto in ["Purchasing", "Shipping", "Manufacturing", "Construction", "Contracting", "Operations"]:
        return "Operações e Logística"
    elif depto in ["Administration", "Executive"]:
        return "Administração Geral"
    else:
        return "Outros"

# Criando a nova coluna no DataFrame de departamentos
df["AREA_NEGOCIO"] = df["DEPARTMENT_NAME"].apply(mapear_area)

# Contar departamentos por área
print("\nQuantidade de departamentos por Área de Negócio:")
print(df["AREA_NEGOCIO"].value_counts())
#Fim do auxílio da IA



###########################################
print("\n\n\nANÁLISE QUERY 2")
######## Média
print("Média de salários entre cargos:")
mediadoscargos = (df2["MIN_SALARY"] + df2["MAX_SALARY"]) / 2
mediaecargos = df2[["JOB_TITLE"]].copy() #o .copy serve para criar um DataFrame totalmente independente

mediaecargos["MEDIA_SALARIO"] = mediadoscargos
print(mediaecargos.to_string()) #o .to_string() serve para exibir o resultado na tela como texto puro


####### Valor mínimo e média
print("\nPiso salarial de cada cargo:")
print(df2[["JOB_TITLE", "MIN_SALARY"]])

print(f"\nMédia de piso salarial: {df2['MIN_SALARY'].mean():.2f}")
valor_minimo = df2["MIN_SALARY"].min()
valor_maximo = df2["MIN_SALARY"].max()
print("Piso salarial mínimo:", valor_minimo)
print("Piso salarial máximo:", valor_maximo)

####### Valor máximo e média
print("\nTeto salarial de cada cargo:")
print(df2[["JOB_TITLE", "MAX_SALARY"]])

print(f"\nMédia de teto salarial: {df2['MAX_SALARY'].mean():.2f}")
valor_minimo2 = df2["MAX_SALARY"].min()
valor_maximo2 = df2["MAX_SALARY"].max()
print("Teto salarial mínimo:", valor_minimo2)
print("Teto salarial máximo:", valor_maximo2)

print("\n\nTotal de cargos:", len(df2))


####### MEDIANA
df2["MEDIA_SALARIO"] = (df2["MIN_SALARY"] + df2["MAX_SALARY"]) / 2
print("Mediana da média de salários:", df2["MEDIA_SALARIO"].median())

quant_piso = (df2["MIN_SALARY"] >= 5000).sum() #Soma todos os cargos com salário minímo de 5000
print("Número de cargos com piso salarial acima de 5000:", quant_piso)


print("\nCargos com piso salarial acima de 5000:")
cargos_piso = df2[df2["MIN_SALARY"] >= 5000][["JOB_TITLE", "MIN_SALARY"]].copy()
cargos_piso["MEDIA_SALARIO"] = mediadoscargos

print(cargos_piso.to_string(index=False))



################################################
######### VIZUALIZAÇÕES

# Faixas salariais por cargo - Média, Piso e Teto Salarial
media = df2.pivot_table( index="JOB_TITLE", values=["MIN_SALARY", "MEDIA_SALARIO", "MAX_SALARY"], aggfunc="mean")

fig, ax = plt.subplots(figsize=(14, max(8, len(media) * 0.45))) #Auxílio da IA para encaixar completamente a escrita
#ax = área do gráfico
# max(8, len(media) * 0.45): define a altura calculada, sendo min. de 8
sns.heatmap(media, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={"label": "Salário"}, ax=ax) #Auxílio da IA

ax.set_title("Faixas salariais por cargo")
fig.tight_layout()
fig.savefig("heatmap_salario_medio.png", bbox_inches="tight") # Remove as bordas brancas desnecessárias ao redor do gráfico
plt.show()

########## Concentração de departamentos por área de atuação
plt.figure(figsize=(10, 5))
df["AREA_NEGOCIO"].value_counts().plot(kind="bar", color="pink") #value_counts() é usado para contar quantas vezes cada categoria única aparece na coluna "AREA_NEGOCIO"

plt.xticks(rotation=45, ha='right') # Deixa os nomes em 45 graus e alinha pela direita para encaixar certinho

plt.title("Quantidade de Ocorrências por Área de Negócio")
plt.ylabel("Quantidade")
plt.tight_layout() 
plt.savefig("bargrafic_concentracao_departamentos.png", bbox_inches="tight") 
plt.show()