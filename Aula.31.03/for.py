
numeros = []

for i in range(10):
    num = int(input(f"Digite o numero {i+1}: "))
    numeros.append(num)

for numero in numeros:
    if numero < 10:
        print(f"O número {numero}, é menor que 10")
    elif numero == 10:
        print(f"O número {numero}, é igual a 10")
    else:
        print(f"O número {numero}, é maior que 10")


numero2 = []

for i in range(6):
    num = int(input(f"Digite um número {i+1}:"))
    numero2.append(num)

for numero in numero2:
    if (numero % 2) == 0:
        print(f"Número {numero}, é par")
    else:
        print(f"Número {numero}, é impar")


numero3 = []

for i in range(7):
    num = int(input("digite um número:"))
    numero3.append(num)

for numero in numero3:
    if numero > 0:
        print(f"Número {numero}, é positivo:")
    elif numero < 0:
        print(f"Número {numero}, é negativo:")
    else:
        print(f"Número {numero}, é igual a 0:")



numero4 = []
contador = 0

for i in range(3):
    num = int(input("Digite um número:"))
    numero4.append(num)

for numero in numero4:
    if numero > 50:
        contador += 1

print("Quantidade de números maiores que 50:", contador)
