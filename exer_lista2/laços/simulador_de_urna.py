bolsonaro = 0
lula = 0
ciro = 0
vnulo = 0
vbranco = 0

cinv = 0
c = 'S'
while c == 'S':
    voto = int(input("bolsonaro <1>  lula <2> ou ciro <3> voto nulo <4> voto branco <5>?:"))
    if voto == 1:
        bolsonaro = bolsonaro + 1
    elif voto == 2:
        lula = lula + 1
    elif voto == 3:
        ciro = ciro + 1    
    elif voto == 4:
        vnulo = vnulo + 1
    elif voto == 5:
        vbranco = vbranco + 1        
    else:
        print("Voto inválido")
        cinv = cinv + 1
    print("")    
    c = input("Deseja Continuar?<S/N>:").upper()
total = bolsonaro + lula + ciro + vnulo + vbranco    
print("Fim da votação")
print("bolsonaro :",bolsonaro,"votos |%.2f"% (bolsonaro/total)*100,"%")
print("lula:",lula,"votos |","%.2f"% (lula/total)*100)
print("ciro",ciro,"votos |","%.2f"% (ciro/total)*100)
print("votos nulos",vnulo,"%.2f"% (vnulo/total)*100)
print("votos brancos",vbranco, "%.2f"% (vbranco/total)*100)
print("Inválidos:",cinv,"%.2f"% (cinv/total)*100)