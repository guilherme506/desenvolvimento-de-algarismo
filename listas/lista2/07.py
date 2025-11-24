#Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como
#par ou ímpar
n = int(input("Digite um número: "))
par = n % 2
if par == 0:
    print("seu numero é par")
else:
    print("seu numero e impar")
