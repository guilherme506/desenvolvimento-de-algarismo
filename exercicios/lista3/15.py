# Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor
# nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente.


numero = []

while True:
    n = float(input("Digite um número (0 para encerrar): "))
    if n == 0:
        break
    numero.append(n)

numero.sort()  # ordena em ordem crescente
    
print("\n--- Números em ordem crescente ---")
for num in numero:
    print(num)

