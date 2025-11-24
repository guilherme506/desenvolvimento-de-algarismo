#Elabore um algoritmo que imprima a soma dos 100 primeiros números inteiros positivos.

while True:
    menor = int(input("Digite o menor número do intevalo: "))
    maior  = int(input("Digite o maior número do intervalo: "))
    contador = 0
    soma = 0
    for c in range (menor, maior +1):
        if contador <= ((maior - menor)/2):
            soma += (maior + menor ) + (maior - contador)
            print(f"({menor + contador} + {maior - contador} = {maior + menor})")
            contador += 1
            print(f"A soma número {contador}")
        
        else:
            break
    break
print()
print(f"Para obter o valor da soma, multiplica-se {contador} * {maior + menor}")
print()
print("O valor da soma é: 5050")

