print("digite seu peso e altura")
altura =float(input("altura "))
peso =float(input("peso "))

imc = peso/(altura*altura)

if imc < 18.5:
     print("Seu IMC é %.2f" % imc)
     print("Abaixo do peso")

elif imc > 18.5 and imc <=25:
    print("Seu IMC é %.2f"% imc)#tratamento pra ficar duas casas apos a ,| %.2f"% #
    print("Peso normal")
elif imc > 25 and imc < 30:
    print("Seu IMC é %.2f"% imc)
    print("Sobre peso") 
elif imc > 30 and imc < 35:
    print("Seu IMC é %.2f"% imc)
    print("Obesidade grau 1")
elif imc > 35 and imc < 40:
    print("Seu IMC é %.2f"% imc)
    print("Obesidade grau 2")        
else:
    print("Seu IMC é ", imc)
    print("Obesidade grau 3")       



    