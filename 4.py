#1
lista = ["bolacha", "amendoin","leite", "macarrão"]
print("Primeiro a ser encontrado:", lista[2])
#2
lista.append("chocolate")
print(lista)
lista.remove("bolacha")
print(lista)
#3
lista2 =[
    float(input("Digite o primeiro número:")),
    float(input("Digite o segundo número:")),
    float(input("Digite o terceiro número:")),
    float(input("Digite o quarto número:"))
]

soma = lista2[0] + lista2[1]
print("Soma dos primeiros números é:", soma)

lista3 = ["4", "5", "6", "7"]
print(lista3)
lista3.remove("5")
print(lista3)

#4 
notas = [
    float(input("Digite a 1º nota:")),
    float(input("Digite a 2º nota:")),
    float(input("Digite a 3º nota:"))
]

media = sum(notas) / len(notas)
print("Media inicial:", media)


menor =min(notas)
print("Menor nota é:", menor)

maior = max(notas)
print("Maior nota é:", maior)

nova = float(input("Digite uma nova nota para substituir a menor:"))
indice = notas.index(menor)
notas[indice] = nova
print(notas)

notas.sort()
nova_media = sum(notas) / len(notas)
print("lista ordenada:", notas)
print("Nova media:", nova_media)

#5
fila = ["Ana", "Bruno"]
print("Fila inicial:", fila)

nomes = [
    input("Digite o proximo nome:"),
    input("Digite o proximo nome:")
]
fila.extend(nomes)
print("Fila após adicionar os nomes:", fila)

prioritario = input("Digite o cliente prioritário:")
fila.insert(0, prioritario)
print("Após inserir prioritário:", fila)

atendido = fila.pop(0)
print("Cliente atendido:", atendido)
print("Fila após atendimento:", fila)

#6
aluno = input("Digite seu nome:")
print("Olá,", aluno)

idade_aluno = int(input("Digite sua idade:"))
print("Sua idade é:", idade_aluno)
print(f"Olá, {aluno} sua idade é {idade_aluno}")
#7
print(f"Olá, {aluno}, sua idade é {idade_aluno} e suas notas seram {notas} com uma media de {nova_media}")

#8
produto = {
    "nome": input("Digite o nome: "),
    "produto": input("Nome do produto: "),
    "preco": 10.5
}
print(produto)

print("Antes:", produto)

produto.pop("desconto", None)

print("Depois:", produto)

#9

produto2 = {
    "nome": input("Nome do produto: "),
    "preco": float(input("Preço: ")),
    "quantidade": int(input("Quantidade: "))
}

percentual = float(input("Percentual de aumento (%): "))

produto2["preco"] += produto2["preco"] * (percentual / 100)

produto2["quantidade"] += 2

total = produto2["preco"] * produto2["quantidade"]

print("\nProduto:", produto2["nome"])
print("Preço atualizado:", round(produto2["preco"], 2))
print("Quantidade atualizada:", produto2["quantidade"])
print("Total:", round(total, 2))

#10
agenda = {
    "Ana": "1111-1111", 
    "Bruno": "2222-2222"
}


nome = input("Novo contato (nome): ")
telefone = input("Telefone: ")
agenda[nome] = telefone


nome_att = input("Nome para atualizar: ")
if nome_att in agenda:
    novo_tel = input("Novo telefone: ")
    agenda[nome_att] = novo_tel
else:
    print("Contato não encontrado.")


nome_remover = input("Nome para remover: ")
if nome_remover in agenda:
    agenda.pop(nome_remover)
else:
    print("Contato não encontrado.")


print("\nContatos ordenados:")
for nome in sorted(agenda.keys()):
    print(nome)

#11

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

tupla = (nome1, nome2)

print("Tupla:", tupla)
print("Tipo:", type(tupla))

#12

fruta1 = input("Digite uma fruta:")
fruta2 = input("Digite uma fruta:")

tupla = (fruta1, fruta2 )

print("Tupla:", tupla)


busca = input("Digite uma fruta para buscar: ")

if busca in tupla:
    print("A fruta está na tupla.")
else:
    print("A fruta NÃO está na tupla.")

#13
numero1 = int(input("Digite o 1º número:"))
numero2 = int(input("Digite o 2º número:"))
numero3 = int(input("Digite o 3º número:"))
numero4 = int(input("Digite o 4º número:"))

tupla2 = (numero1, numero2, numero3, numero4)
print(tupla2)
busca = int(input("Digite um número para contar:"))
quantidade = tupla2.count(busca)
print("O número aparece", quantidade, "vez(es) na tupla.")
#14
menor =min(tupla2)
print("Menor número é:", menor)

maior1 =max(tupla2)
print("Maior número é:", maior1)

#15
dias_semana = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
)

print(dias_semana)

#16

notas1 = (
    float(input("Digite a 1º nota:")),
    float(input("Digite a 2º nota:")),
    float(input("Digite a 3º nota:"))
)
media1 = sum(notas1) / len(notas1)
print("Media inicial:", media1)
print("Media:", round(media1, 2))
 
 #17
numero5 = int(input("Digite o 1º número:"))
numero6 = int(input("Digite o 2º número:"))
numero7 = int(input("Digite o 3º número:"))
numero8 = int(input("Digite o 4º número:"))

tupla3 = (numero5, numero6,numero7, numero8)
print("Tupla original:", tupla3)

lista_ordenada = sorted(tupla3)
print ("Lista ordenada:", lista_ordenada)

print("Tipo da variável ordenada:", type(lista_ordenada))
