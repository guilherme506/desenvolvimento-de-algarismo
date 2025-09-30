#Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o
#maior e o menor deles.

numero = []
for c in range (10):
    while True:
        try:    
            n1 = float(input(f"Digite o {c + 1} número: "))
            numero.append(n1)
        except ValueError:
            print("Entrada não permitida. Por favor tente novamente ")
        break

numero.sort()
for numeros in numero:
    print(numeros)