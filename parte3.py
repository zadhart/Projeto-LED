import pandas as pd
from sklearn.preprocessing import LabelEncoder

'''
    Esse código tem como objetivo fazer uma exploração temporal da evolução das bases de dados que podem ser
encontradas nos seguintes links:
    
    base1: https://drive.google.com/drive/folders/1oMnWg210cRmBszkUXxOU9bBED7PBcN2F?usp=sharing
    base2: https://drive.google.com/drive/folders/1dxZtKwguN2l6ho7zBvxdM_Spi-r6_SYQ?usp=sharing
    
    Assim como outra base de dados utilizada nesse projeto, essas também estão com um formato dificil de 
se trabalhar. Portanto, portanto utilizamos o código: parte2.py para converter as bases para um formato
mais simples.
'''

def remv(s):
    #Essa função remove todos os caracteres não numéricos de uma string
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_s = ""
    for x in s:
        if(x in num):
            new_s = new_s + x
    return int(new_s)

#Lendo o csv em um dataframe
data1 = pd.read_csv("dados_1806NOVO.csv")

data2 = pd.read_csv("dados_1906NOVO.csv")

#Vamos encontrar o número de novos registros
print("Numero de novos registros: " + str(len(data2) - len(data1)))

print("---------------------------------------------------")

#Vamos tentar dar um match nos registros
i = 0
for x in data1["document_id"]:
    if(x in data2["document_id"]):
        i += 1
print("Registros iguais document_id: " + str(i))

print("---------------------------------------------------")
i = 0
for x in data1["paciente_id"]:
    if(x in data2["paciente_id"]):
        i += 1
print("Registros iguais paciente_id: " + str(i))

print("---------------------------------------------------")

'''
    Com isso fica evidente que não podemos usar os valores dessas colunas para dar um match nos registros.
    
    Portanto, vamos usar uma outra estratégia. Vamos criar vetores para descrever os registros, portanto
vetores iguais devem descrever um mesmo registro que foi inalterado, e como já sabemos quantos novos registros
foram criado podemos ter uma estimativa de quantos registros foram modificados através da equação:

                            TOTAL - NOVOS - IGUAIS = MODIFICADOS 
                            
    Então para isso precisamos transformar as variáveis categoricas em variáveis numéricas para então criar os
vetores descritivos.
'''

#Removendo algumas colunas desnecessárias
new_data1 = data1.drop(['document_id', 'paciente_id', 'id_sistema_origem'], 1)
new_data2 = data2.drop(['document_id', 'paciente_id', 'id_sistema_origem'], 1)

#Preenchendo todos os valores ausentes com 0
new_data1 = new_data1.fillna(0)
new_data2 = new_data2.fillna(0)

#Convertendo os valores da coluna paciente_datanascimento (DATA1)
paciente_datanascimentoCON = []
for x in new_data1["paciente_datanascimento"]:
    paciente_datanascimentoCON.append(remv(str(x)))

#Convertendo os valores da coluna vacina_dataaplicação (DATA 1)
vacina_dataaplicacaoCON = []
for x in new_data1["vacina_dataaplicacao"]:
    vacina_dataaplicacaoCON.append(remv(str(x)))

#Convertendo os valores da coluna data_importacao_rnds (DATA 1)
data_importacao_rndsCON = []
for x in new_data1["data_importacao_rnds"]:
    data_importacao_rndsCON.append(remv(str(x)))

#Exluindo as colunas antigas
new_data1 = new_data1.drop(["data_importacao_rnds", "vacina_dataaplicacao", "paciente_datanascimento"], axis=1)

#Adicionando as novas colunas
new_data1.insert(len(new_data1.columns), "paciente_datanascimentoCON", paciente_datanascimentoCON, True)
new_data1.insert(len(new_data1.columns), "vacina_dataaplicacaoCON", vacina_dataaplicacaoCON, True)
new_data1.insert(len(new_data1.columns), "data_importacao_rndsCON", data_importacao_rndsCON, True)

#Convertendo os valores da coluna paciente_datanascimento (DATA 2)
paciente_datanascimentoCON = []
for x in new_data2["paciente_datanascimento"]:
    paciente_datanascimentoCON.append(remv(str(x)))

#Convertendo os valores da coluna vacina_dataaplicação (DATA 2)
vacina_dataaplicacaoCON = []
for x in new_data2["vacina_dataaplicacao"]:
    vacina_dataaplicacaoCON.append(remv(str(x)))

#Convertendo os valores da coluna data_importacao_rnds (DATA 2)
data_importacao_rndsCON = []
for x in new_data2["data_importacao_rnds"]:
    data_importacao_rndsCON.append(remv(str(x)))

#Excluindo as colunas antigas
new_data2 = new_data2.drop(["data_importacao_rnds", "vacina_dataaplicacao", "paciente_datanascimento"], axis=1)

#Adicionando as novas colunas
new_data2.insert(len(new_data2.columns), "paciente_datanascimentoCON", paciente_datanascimentoCON, True)
new_data2.insert(len(new_data2.columns), "vacina_dataaplicacaoCON", vacina_dataaplicacaoCON, True)
new_data2.insert(len(new_data2.columns), "data_importacao_rndsCON", data_importacao_rndsCON, True)


#Vamos criar o label_encoder a partir da biblioteca scikit-learn
label_encoder = LabelEncoder()

#Colunas com variaves categoricas
colunas_categoricas = ['paciente_enumsexobiologico', 'paciente_racacor_valor', "paciente_endereco_nmmunicipio",
                       "paciente_endereco_nmpais", "paciente_endereco_uf", "paciente_nacionalidade_enumnacionalidade",
                       "estabelecimento_razaosocial", "estalecimento_nofantasia", "estabelecimento_municipio_nome",
                       "estabelecimento_uf", "vacina_grupoatendimento_nome", "vacina_categoria_nome",
                       "vacina_lote", "vacina_fabricante_nome", "vacina_fabricante_referencia",
                       "vacina_descricao_dose", "vacina_nome", "sistema_origem"]

#Transformando as variaveis categoricas em variaveis numericas
for x in colunas_categoricas:
    new_data1[x] = label_encoder.fit_transform(new_data1[x])
    new_data2[x] = label_encoder.fit_transform(new_data2[x])

#Vamos guardar os resultados em novos CSVs porque esse código demora para rodar
new_data1.to_csv("new_data1806.csv", index=False)
new_data2.to_csv("new_data1906.csv", index=False)
