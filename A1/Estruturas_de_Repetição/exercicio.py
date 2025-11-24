#Utilizando for
print("Números pares de 1 a 100: ")
for num in range(1, 101):
    if num % 2 == 0:
        print(num)


print('_-_' * 30)


#Utilizando while
print("Números pares de 1 a 100:")
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
