#algoritimo identificacao de flores (margarida e girassol)
#caracteristicas dos dados (1=sim/0=nao)
#petala amarela
#tem semente
#acompanha o sol

#1=margarida
margarida1 = [0, 0, 0]
margarida2 = [1, 0, 0]
margarida3 = [1, 0, 0]


#0=girassol
girassol1 = [1, 1, 1]
girassol2 = [1, 1,  0]
girassol3 = [1,  1, 0]

dados = [margarida1, margarida2, margarida3, girassol1, girassol2, girassol3]
classes = [1,1,1,0,0,0]

from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit (dados, classes)

flor_misteriosa = [1,1,1]
model.predict([flor_misteriosa])

flor_desconhecida1=[1,1,1]
flor_desconhecida2=[0,1,0]
flor_desconhecida3=[1,0,1]

# p/ ver eficacia da predict 
teste = [flor_desconhecida1, flor_desconhecida2, flor_desconhecida3]
previsoes = model.predict(teste)

testes_classes = [0,1,1]


corretos = (previsoes == testes_classes).sum()
total = len(teste)
taxa_de_acertos = corretos/total
print("taxa de acerto é", int(taxa_de_acertos * 100))