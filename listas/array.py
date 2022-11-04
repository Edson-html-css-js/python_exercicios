# marcas = ["Asus","dell","mac","hp"]
# print(marcas[0:3])#pegando da posição 0 até a 3 que no caso é a 2

# print(len (marcas))#vendo o tamanho da lista
# marcas.append("positivo")#adcionando mais um nome na lista
# print(marcas)

# paises = ["basil","africa","russia","belgica"]
# print(paises)

# cliente = ["lucad","(11)98026-2609", 31]
# print(cliente)

mv = 0
idade = [23,21,20,45]

for i in range(0,4):#percorendo a lista toda
    print(idade[i])
    if idade[i]>idade[mv]:#tratamento pra inprimir o maior numero
        mv = i
print("A idade mais velha é :", idade[mv])
