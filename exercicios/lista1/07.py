#Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final
#apresente na tela os dois números informados formatando com duas casas decimais
#somente o número real da seguinte forma: "Voce informou os numeros N e X.YY"
n1 = int(input("Digite um número inteiro: "))
real = float(input("Digite um número real: "))
soma = n1 + real
print(f"Você informou os números {n1:.2f} é {real:.2f} é a soma deles deu {soma:.2f}")