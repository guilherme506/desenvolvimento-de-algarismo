#Elabore um algoritmo que solicite ao usuário uma palavra e um número inteiro que
#indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada
#linha.
p = str(input("Escreva uma palavra: "))
n = int(input("Escreva um número: "))

for i in range(n):
    print(p)
