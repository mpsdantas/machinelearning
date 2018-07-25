#coding: utf-8


#Conjunto de dados ficticios.
#Criterio de Classificação:
# É gordo ?
# Tem perna curta ?
# Late ?
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]


#Junção dos dados.
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

#marcação do que é cada dado: porco ou cachorro. Porco = 1, Cachorro = -1.
marcacoes = [1, 1, 1, -1, -1, -1]

#Dois dados misteriosos para ser testados pela rede.
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

#junção do arrei de dados misteriosos.
teste = [misterioso1, misterioso2, misterioso3]

from sklearn.naive_bayes import MultinomialNB #importando a classe MultinomialNB

modelo = MultinomialNB() #Instanciando a classe MultinomialNB.
modelo.fit(dados,marcacoes) #Treinamento da rede.
#OBS o metodo fit deve ser passado os dados e o que cada um é.

marcacoes_teste = [-1, 1, -1]

#Exibindo o resultado de cada rede.
resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste)
taxa_de_acertos = 100.0 * total_de_acertos/total_de_elementos
print(resultado - marcacoes_teste)
print(acertos)
print(taxa_de_acertos)
for i in range(len(resultado)):
	if resultado[i]==1:
		print("O misterioso" + str(i+1) + " é porco.")
	else:
		print("O misterioso" + str(i+1) + " é cachorro.")


