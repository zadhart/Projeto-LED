import pandas as pd

#Resolvemos fazer o tratamento dos dados usando python e a biblioteca pandas

#Lendo os dados em um dataframe
data = pd.read_csv("dataALcovid.csv")

#Checando os dados que estão faltando
print(data.isnull().sum())

#Tratando as anomalias da coluna "paciente_idade"
i = 0
#Vamos guardar a posição de todas as linha que queremos remover
drop_index = []
for x in data["paciente_idade"]:
    #   Retiramos os valores menores que 18 por razões óbvias, já maiores que 118 porque a pessoa mais velha do
    #mundo atualmente tem 118 anos

    if(x < 18 or x > 118):
        drop_index.append(i)
    i += 1
#Vamos remover todas as linhas selecionadas
data = data.drop(drop_index)

#   Não vamos remover mais linha com dados faltando porque perderíamos muitas informações importantes,
#e ganharíamos muito pouco, visto que a maior parte das informações importantes como a idade e o
#sexo biológico estão presentes.