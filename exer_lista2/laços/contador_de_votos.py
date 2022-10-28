ccoca = 0
cpepsi = 0
cinv = 0
c = 'S'
while c == 'S':
    voto = int(input("Coca <1> ou Pepsi <2>?:"))
    if voto == 1:
        ccoca = ccoca + 1
    elif voto == 2:
        cpepsi = cpepsi + 1
    else:
        print("Voto inválido")
        cinv = cinv + 1
    print("")    
    c = input("Deseja Continuar?<S/N>:").upper()
print("Fim da votação")
print("Coca :",ccoca,"votos")
print("Pepsi:",cpepsi,"votos")
print("Inválidos:",cinv,"votos")