#Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da
#pessoa mais pesada
n1 = str(input("Digite um nome: "))
p1 = float(input("Qual é o peso dessa pessoa: "))
n2 = str(input("Digite um nome: "))
p2 = float(input("Qual é o peso dessa pessoa: "))
if p1 > p2:
    print(f"A {n1} é mais pesada do que a {n2}")
else:
    print(f"A {n2} é mais pesada do que a {n1}")
    