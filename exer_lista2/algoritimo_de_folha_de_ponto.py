vHora = float(input("valor por hora em R$ "))
qHora =float(input("quantidade de horas trabalhadas"))

salario = (vHora*qHora)

if salario <= 900:
    pir = 0
elif salario <= 1500:
    pir = 0.05
elif salario <= 2500:
    pir = 0.10
else:
    pir = 0.20

vl_ir = salario* pir
        

print("salario bruto", salario)

print("Ir = R$", salario % 95)
print("INSS = R$", salario % 90)
print("Seu FGTS É R$ ", salario )
