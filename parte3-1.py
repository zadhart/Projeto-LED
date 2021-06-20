import pandas as pd
import math

'''
    Esse código tem como objetivo UM match entre dois registros em dois dataframes distintos.
    
    Não vamos tentar encontrar um match para cada registro porque essa é uma tarefa
computacionalmente complexa. E, nesse momento não disponho do tempo nem do poder computacional para tentar
encontrar registros iguais em um dataset dessa magnitude.
    Portanto esse é apenas um código ilustrativo que tem como função apenas mostrar que é possível
encontrar registros semelhantes usando esse método
'''

#Essa função calcula a distancia entre dois vetores
def get_distance(vector1, vector2):
    dist = 0
    for x in range(len(vector1)):
        dist += (vector1[x] - vector2[x]) * (vector1[x] - vector2[x])
    return math.sqrt(dist)

#Vamos ler o csv como um dataframe
data1 = pd.read_csv("new_data1806.csv")
data2 = pd.read_csv("new_data1906.csv")

#Vamos transformar os dataframes em listas
data1_list = data1.values.tolist()
data2_list = data2.values.tolist()

#Vamos tentar encontrar um match ;)
i = 0
for x in data1_list:
    for y in data2_list:
        d = get_distance(x, y)
        if(d < 1):
            print("YES")
            print(d)
            break
    break


