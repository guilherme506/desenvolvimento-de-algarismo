#16. Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido
#no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.
fixo = float(input("Salário fixo: "))
tot = float(input("Total vendido: "))
per = float(input("percentual de comissão(%): "))
salario = fixo + (tot *(per /100) )
print(f"O salario bruto foi de {salario}")