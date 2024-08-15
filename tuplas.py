#Definindo nossa primeira tupla
tuplal = ("gato", "cachorro", "papagaio", "tartaruga")
print(tuplal)

#criando um intervalo de uma tupla; mesmo formato das listas, com colchetes
print(tuplal[2])

#acessando um da tupla; mesmo formato das listas
print(tuplal[1:3])

#criando uma tupla vazia
tupla_vazia = ()
print(tupla_vazia)

#não é possivel fazer a alteração de um elemento da tupla; python retorna um erro
tuplal[tuplal] = "elefante"

#para apagar uma tupla, use-se de ()
# del(tuplal)
# print(tuplal)

#algumas funções para se trabalhar com tuplal
tupla2 = (8.3, 9.4, 3.3, 7.5, 7.6)
print(max(tupla2))
print(min(tupla2))
print(len(tupla2))

#transformando uma tupla  em lista e vice-versa
listal = list(tuplal)
print(listal)
lista2 = ["josé", "afonso", "carlos", "luiz"]
tupla3 = tuple(lista2)
print(tupla3)