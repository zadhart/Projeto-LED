import pandas as pd

#Lendo o csv como um dataframe
data = pd.read_csv("us-500.csv")

#Checando por dados faltando
print(data.isnull().sum())


#Removendo todos os zip codes irregulares
i = 0
for x in data["zip"]:
    if(len(str(x)) != 5):
        data = data.drop(i)
    i += 1


#Separando a coluna address

#Vamos criar três novas colunas do dataframe
num_rua = []
nome_rua = []
num_quartos = []

for x in data["address"]:
    lista = x.split()

    num = lista[0]
    lista.pop(0)
    nrua = ""
    quartos = "NaN"

    if(lista[-1][0] == "#"):
        quartos = lista[-1]
        lista.pop(-1)

    for y in lista:
        nrua = nrua + " " + y

    num_rua.append(num)
    nome_rua.append(nrua)
    num_quartos.append(quartos)

#Colocando as novas colunas no dataframe
data.insert(len(data.columns), "num_rua", num_rua, True)
data.insert(len(data.columns), "nome_rua", nome_rua, True)
data.insert(len(data.columns), "num_quartos", num_quartos, True)


#Classificando os endereços por "state"
data_states = {}
for x in data["state"].unique():
    data_states[x] = data[data["state"] == x]








