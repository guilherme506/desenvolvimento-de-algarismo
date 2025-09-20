#Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o
#número informado é positivo, negativo ou nulo (zero)
n1 = float(input("Digite um número: "))
if n1 > 0:
    print("Seu número è positivo")
elif n1  < 0:
    print("Seu número é negativo")
else:
    print("Seu número é nulo")