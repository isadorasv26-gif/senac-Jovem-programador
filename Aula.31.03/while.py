
resposta = ''

while resposta != 'ola':
    resposta = input('Digite algo (ou "ola" para encerrar):')
    print(f'Você digitou: {resposta}')



while True:
    resposta = input('Digite algo (ou "ola" para encerrar):').lower().strip()
    if resposta != 'ola':
        print(f'Você digitou: {resposta}')
        continue
    else:
        break

#atividade

total = 0
quantidade = 0
valor = -1 

while valor != 0:
    valor = float(input("Digite o valor da compra (0 para encerrar): "))
    
    if valor != 0:
        total += valor
        quantidade += 1

if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("Total das compras:", total)
print("Quantidade de compras:", quantidade)
print(f"Valor médio: {media}")


