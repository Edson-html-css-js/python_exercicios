print("digite seu peso e altura")
altura =float(input("altura"))
peso =float(input("peso"))

imc = peso/(altura*altura)

if imc>=18 and imc <=24:
     print("seu imc está normal")

elif imc<=18:
    print("você está muitomagro")
elif imc>30:
    print("você está obeso")    