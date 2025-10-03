#Escreva um programa que vá solicitando as idades dos alunos da sala até que todos
#sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao
#final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de
#18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana.

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:  # número par de elementos
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:  # número ímpar de elementos
        return lista_ordenada[meio]

idades = []

while True:
    idade = int(input("Digite a idade do aluno: "))
    idades.append(idade)

    continuar = input("Deseja informar a idade do próximo aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break

if len(idades) > 0:
    mais_novo = min(idades)
    mais_velho = max(idades)
    mais_de_18 = sum(1 for idade in idades if idade > 18)
    ate_18 = sum(1 for idade in idades if idade <= 18)
    media = sum(idades) / len(idades)
    mediana = calcular_mediana(idades)

    print("\n--- Resultado ---")
    print(f"Mais novo: {mais_novo}")
    print(f"Mais velho: {mais_velho}")
    print(f"Alunos com mais de 18 anos: {mais_de_18}")
    print(f"Alunos com até 18 anos: {ate_18}")
    print(f"Média aritmética: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
else:
    print("Nenhuma idade foi informada.")
