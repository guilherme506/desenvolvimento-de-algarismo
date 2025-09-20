#Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado
#seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
soma = n1 + n2
if soma > 10:
    print(soma**2)
else:
    print(soma/2)