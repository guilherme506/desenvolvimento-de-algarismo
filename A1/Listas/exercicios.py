alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for n in range(quantidade):
    nome = input(f"Digite o nome do aluno {n+1}: ")
    alunos.append(nome)

print("\nLista de alunos cadastrados:")
for nome in alunos:
    print("-", nome)
