import pandas as pd

'''
    Esse código tem como objetivo fazer uma exploração temporal da evolução das bases de dados que podem ser
encontradas nos seguintes links:

    base1: https://drive.google.com/drive/folders/1oMnWg210cRmBszkUXxOU9bBED7PBcN2F?usp=sharing
    base2: https://drive.google.com/drive/folders/1dxZtKwguN2l6ho7zBvxdM_Spi-r6_SYQ?usp=sharing

    Assim como outra base de dados utilizada nesse projeto, essas também estão com um formato dificil de 
se trabalhar. Portanto, portanto utilizamos o código: parte2.py para converter as bases para um formato
mais simples.
'''
#Lendo o csv em um dataframe
data1 = pd.read_csv("dados_1806NOVO.csv")

data2 = pd.read_csv("dados_1906NOVO.csv")

#Vamos encontrar os registros que possuem o mesmo document_id
match = []
for x in data1["document_id"]:
    for y in data2["document_id"]:
        if(x == y):
            match.append(x)
            break

print("Registros iguais: " + str(len(match)))

print("---------------------------------------------------")

#Vamos encontrar os registros excluidos
excluidos = []

for x in data1["document_id"]:
    if(x not in match):
        excluidos.append(x)

print("Excluidos: " + str(len(excluidos)))

print("---------------------------------------------------")

#Vamos encontrar o número de novos registros
novos = []

for x in data2["document_id"]:
    for y in data1["document_id"]:
        if(x == y):
            novos.append(x)
            break

print("Novos registros: " + str(len(novos)))
