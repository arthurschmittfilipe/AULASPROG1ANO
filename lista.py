# criando uma lista de fruta
frutas = ["maçã", "banana", "uva"]

#criando uma nova fruta
frutas.append("morango")

#imprimindo a lista atualizada
print(frutas) # saída: ["maçã", "banana", "uva", "morango"]

# removendo a banana
frutas.remove("banana")

#imprimindo a lista novamente
print(frutas) # saída: ["maçã", "uva", "morango"]

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)