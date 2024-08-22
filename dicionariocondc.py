from typing import Dict

dados = {"nome": "arthur", "idade": 14}
if "cidade" in dados:
    dados["cidade"] = "rio de janeiro"
else:
    dados["cidade"] = "são paulo"
print(dados)

dados2 = {"produto": "caixão", "preço": 50}
if "desconto" in dados2:
    print(oi)
else:
    dados2["desconto"] = 10
print(dados2)

dados3 = {"nome": "arthur", "idade": 14}
if dados3["idade"] >= 18:
    dados3["+18"] = True
else:
    dados3["+18"] = False
print(dados3)

dados4 = {"a": 1, "b": 2, "c": 3, "d": 4}
if "d" in dados4:
    print("d está no d icionario")
else:
    dados4["d"] = 4
    print("d foi adicionado")