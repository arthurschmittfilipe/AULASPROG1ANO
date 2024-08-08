frutas = ["maçã", "banana", "melancia", "uva", "bergamota"]
print(frutas)

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numero[0], numero[2], numero[9])

lista = []
lista.append(5)
lista.append(10)
lista.append(15)
lista.remove(10)
print(lista)

semana=["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
print(len(semana))

paises = ["brasil", "estados unidos", "rússia", "argentina", "alemanha"]
if "brasil" in paises:
    print("brasil está na lista")
else:
    print("brasil não está na lista")