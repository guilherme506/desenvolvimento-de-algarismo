#Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se
#são iguais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if n1 == n2:
    print("Os números são iguais")
elif n1 > n2:
    print(f"O número {n1} é maior do que o {n2}")
else:
    print(f"O número {n2} é maior do que o {n1}")