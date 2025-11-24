idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade <= 14:
    print("Entrada proibida para menores de 14 anos.")
elif idade < 18:
    print("Entrada permitida somente acompanhado de responsável.")
else:
    print("Entrada liberada! Aproveite o evento.")
