# lista: representa uma sequencia de valores

# sintaxe: nome_da_lista = [valores]
notas = [5,7,8,6,9]
print(notas)

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
print(valores)
print(type(valores))

print(valores[0])
# ultimo valor
print(valores[-1])
# penultimo valor
print(valores[-2])

valores[0] = 9
print(valores[0])
# a partir da posição 0, imprime 2 valores
print(valores[0:2])
# a partir da posição 0, imprime 4 valores
print(valores[:4])
# a partir do penultimo ate o fim
print(valores[-2:])

# quantos elementos tem na lista
print(len(valores))
# retorna versao ordenada da lista
print(sorted(valores))
print(sorted(valores, reverse=True))
print(min(valores))
print(max(valores))

# acrescenta um novo valor no fim da lista
valores.append(13)
print(valores)
# remove o ultimo elemento da lista
valores.pop()
print(valores)
# remove elemento na posição 3
valores.pop(3)

#insere na posição 3 o valor 21
valores.insert(3, 21)
print(valores)
# imprime se 17 esta na lista
print(17 in valores)

# planetas = list()  -> cria uma lista vazia

planetas = ['Mercurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)

#exercicio
bebidas = []
for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)
bebidas.sort()
print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)
print(f'\nSaúde!')

