# Sintaxe:
# print(objetos, argumentos)

mensagem = 'Função print()'
print(mensagem)
print('Aula de Python')


nome = 'Suely Rodrigues'
print('Bóson Treinamentos -', nome)

nome = input('Digite seu nome: ')
msg = print('Olá '+ nome +'! Bem-vinda ao curso de Python!')
print(msg)
print('outro texto')

print('imprime a msg e permanece na linha.', end='')

nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)

# F String:
nome = 'Suely'
peso = 113
msg = f'Olá, meu nome é {nome} e eu peso {peso}kg.'
print(msg)

valor = 125.579637
print(f'o valor é {valor:.f}')
#caractere de escape:
print(f'o valor é \'{valor}\'')
#tabulação
nome = 'João'
idade = 32
print(f'Nome: {nome}\tIdade: {idade}')


