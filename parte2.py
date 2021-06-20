import pandas as pd

'''
        Todo esse código tem como objetivo converter o dataset disponível no 
    link: https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/ef3bd0b8-b605-474b em um
    dataset com um formato mais legível e mais simples de se trabalhar/analisar.
'''


def remv(s):
    #Essa função tem como objetivo remover o caracter " de uma string
    new_s = ""
    for x in range(len(s)):
        if (s[x] != "\""):
            new_s = new_s + str(s[x])

    return new_s

#Vamos ler o arquivo csv em um dataframe
data = pd.read_csv("part-00000-c04f74bd-6d4f-4253-bfd8-2a679a5b3831.c000.csv")

#Vamos pegar os nomes das colunas do dataset e organizá-los
column_name = data.columns[0]
column_name = str(column_name)
new_column_name = remv(column_name)

#Vamos criar um dicionário que vai guardar os dados do novo dataset
data_dic = {}
data_columns = new_column_name.split(";")
for x in data_columns:
    data_dic[x] = []

#Nessa parte percorremos o dataframe coletando os dados e organizando o dicionário criado anteriormente
for x in range(100000):
    ndata = data[column_name][x]
    ndata = str(ndata)
    ndata = remv(ndata)
    ndata = ndata.split(";")

    for y in range(len(ndata)):
        data_dic[data_columns[y]].append(ndata[y])

#Transformamos o dicionário em um dataframe, e o exportamos como um novo csv
new_datafr = pd.DataFrame.from_dict(data_dic)
new_datafr.to_csv("100000dataALcovid.csv", index=False)




