# for item in sequencia:
#   instruções executadas para cada item da sequencia

lista = [2, 6, 9, 4, 0, 12, 3, 7]    
for item in lista:
    print(item)

palavra = 'Bóson'
for letra in palavra:
    print(letra)


for numero in range(1, 11):
    print(numero)

for numero in range(10):
    print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
for x in range(2, 20, 2):
    print(x)
# range inverso:
for x in range(20, 2, -2):
    print(x)


pedras = ('rubi', 'esmeralda', 'quartzo', 'safira', 'diamante', 'turmalina')
for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)