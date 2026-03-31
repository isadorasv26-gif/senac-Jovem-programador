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
        
