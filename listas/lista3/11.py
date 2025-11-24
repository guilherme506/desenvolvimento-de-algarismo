#Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
#números a serem lidos. Em seguida, leia n números (conforme o valor informado
#anteriormente) e imprima a soma e a média aritmética dos números informados.

soma = 0
n = int(input("Digite um número de entrada que indicará a quantidade de vezes que a palavra vai ser lida: "))

for c in range(1, n+1):
    soma = soma + c
    print(c)


media = (soma/n)
print(f"A soma dos números foi de {soma} é a média foi de {media}")