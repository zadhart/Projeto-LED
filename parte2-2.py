import pandas as pd

#Resolvemos fazer o tratamento dos dados usando python e a biblioteca pandas

#Lendo os dados em um dataframe
data = pd.read_csv("100000dataALcovid.csv")

#Checando os dados que estão faltando
print(data.isnull().sum())

#Tratando as anomalias da coluna "paciente_idade"
i = 0
#Vamos guardar a posição de todas as linhas que queremos remover
drop_index = []
for x in data["paciente_idade"]:
    #   Retiramos os valores menores que 18 por razões óbvias, já maiores que 118 porque a pessoa mais velha do
    #mundo atualmente tem 118 anos

    if(x < 18 or x > 118):
        drop_index.append(i)
    i += 1

#Tratando todos os dados em falta na coluna paciente_racacor_valor:
i = 0

#Guardando a posição de todas as linhas que queremos remover
for x in data["paciente_racacor_valor"]:
    if(x == "SEM INFORMACAO"):
        if(i not in drop_index):
            drop_index.append(i)
    i += 1

#Vamos remover todas as linhas selecionadas
data = data.drop(drop_index)

#Vamos remover as linhas que possuem dados faltando.

#Selecionando as colunas
columns_to_drop = []
for x in data.columns:
    #Exceto os dados da coluna "id_sistema_origem"
    if(x != "id_sistema_origem"):
        columns_to_drop.append(x)

#Removendo os dados
data = data.dropna(subset= columns_to_drop)

print(data.isnull().sum())

#Salvando o novo dataframe em um csv
data.to_csv("100000dataALcovidFinal.csv", index=False)
