import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

dados = pd.read_csv('data.csv', delimiter=',')
dados = dados.drop(dados.columns[[4]], axis=1)

s1 = np.zeros((1,49))
s2 = np.zeros((1,50))
s3 = np.zeros((1,50))
s1 = s1 + 1
s2 = s2 + 2
s3 = s3 + 3

marcacoes = pd.Series(np.append(s1[0],[s2[0],s3[0]]))
print(marcacoes)
modelo = MultinomialNB() #Instanciando a classe MultinomialNB.
modelo.fit(dados,marcacoes) #Treinamento da rede.

# Amostras
misterioso1 = [5.1,3.5,1.4,0.2]
misterioso2 = [5.0,3.4,1.5,0.2]
misterioso3 = [6.0,3.0,4.8,1.8]
marcacoes_teste = [1, 1, 3]

#junção do arrei de dados misteriosos.
teste = [misterioso1, misterioso2, misterioso3]

#Exibindo o resultado de cada rede.
resultado = modelo.predict(teste)
diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d==0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)
taxa_de_acertos = 100.0 * total_de_acertos/total_de_elementos

print('Taxa de acertos', taxa_de_acertos)

for i in range(len(resultado)):
    if resultado[i]==1:
        print("O misterioso" + str(i+1) + " é Iris-setosa.")
    elif resultado[i]==2:
        print("O misterioso" + str(i+1) + " é Iris-versicolor.")
    elif resultado[i]==3:
        print("O misterioso" + str(i+1) + " é Iris-virginica.")
	
		
    