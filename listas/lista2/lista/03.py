#Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o
#número informado é maior que dez, se é menor que dez, ou se é igual a dez
n1: float = float(input("Digite um número real: "))
if n1 > 10:
    print("o numero informado e maior do que 10")
elif n1 < 10:
    print("seu numero é menor do que 10")
else:
    print("Seu número é igual a dez ")