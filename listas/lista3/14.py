#Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o
#maior e o menor deles.
maior = None
menor = None

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

