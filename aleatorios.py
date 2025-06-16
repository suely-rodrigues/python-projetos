import random

# num aleatorio entre 1 e 20
valor = random.randint(1,20)
print(valor)

# cinco num aleatorios entre 1 e 50
print('Gerar cinco num aleatorios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1, 50)
    print(f'Num gerado: {n}')

# gerar num float
# random -> gera float entre 0 e 1
valor = random.random()
print(valor)

# float entre 0 e 10
print(valor*10)
# arredondando com round
print(round(valor*10, 2))

# gera direto o float
valor = random.uniform(1, 10)
print(valor)
# arredondando
print(round(valor, 4))

# escolhe um valor em uma lista
L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(L)
print(n)
# escolhe + de 1 valor
m = random.sample(L, 3)
print(m)
# embaralhar
print(L)
e = random.shuffle(L)
print(L)
