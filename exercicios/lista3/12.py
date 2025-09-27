#Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
#registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N
#pessoas e ao final apresentar o nome da pessoa mais velha
nome_velho = ""
idade_velho = -1
n= int(input("Digite um número de entrada que indicará a quantidade de vezes que a palavra vai ser lida: "))
for pess in range(1, n+1):
    print(f"____{pess}° pessoa _____")
    nome = str(input("Nome: ")).strip().lower()
    idade = int(input("Idade: "))
    if idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
print(f"O nome da pessoa mais velho é {nome_velho} com a idade de {idade_velho} anos")