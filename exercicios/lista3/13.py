#Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
#registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N
#pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados.
mulher = 0
homem = 0
tot_m= 0
tot_f=-0
n = int(input("Digite um número de entrada que indicará a quantidade de vezes que a palavra vai ser lida: "))
for pess in range(1, n+1):
    print(f"____{pess}° pessoa _____")
    nome = str(input("nome: ")).strip().lower()
    idade = int(input("idade: "))
    genero = str(input("gênero(m,f): ")).strip().lower()
    if genero =="m":
        tot_m += 1
        homem = homem + idade
    if genero =="f":
        tot_f +=  1
        mulher = mulher + idade

media_m = mulher/tot_m
media_f = homem/tot_f

print(f"A média da idade do grupo é femininos foi de {media_f} tendo no total {tot_f} integrantes femininos")
print(f"A média da idade do grupo é masculino foi de {media_m} tendo no total {tot_m} integrantes masculinos") 
