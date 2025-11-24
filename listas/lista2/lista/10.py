#O sistema de avaliação de determinada disciplina é composto por três provas. A primeira
#prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Considerando que a
#média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno
#desta disciplina e dizer se o aluno foi aprovado ou não
p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
p3 = float(input("Digite a terceira nota: "))

media = ((p1 * 2) + (p2 * 3) + (p3 * 5))/10
if media > 6:
    print("aprovado")
else:
    print("reprovado")