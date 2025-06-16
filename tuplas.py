# Tuplas são imutáveis
tupla = (2,4,6,7,9)
print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(len(halogenios))
print(halogenios[2])
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print(elementos)

t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
#quantas vezes aparece o num 5
print(t1.count(5))

#imprimir de posição 0 a 2
print(halogenios[0:2])
#está presente?
print('Fe' in halogenios)

#somatorio
print(sum(t1))

# Operações não disponiveis em Tupla: amétodos que alteram conteúdo. imutável


# criar lista a partir de uma tupla
grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)

# criar tupla a partir de lista
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

# criar nova tupla com elementos ordenados
print(sorted(alcalinos))
#print(alcalinos.sort()) -> erro
