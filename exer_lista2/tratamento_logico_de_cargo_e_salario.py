cargo = input("cargo").lower()
salario = float(input("salario R$"))

if cargo == "progamador de sistemas":
    aumento = 0.30
elif cargo == "analista de sistemas":
    aumento = 0.20
elif cargo == "analista de banco de dados":
    aumento = 0.15
else:
    aumento = 0
valor_aumento = aumento * salario
novo_salario = salario + valor_aumento
print(" O novo salario é de R$", novo_salario)                