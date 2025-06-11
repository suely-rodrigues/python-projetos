nome = 'Suely'
# nome_usuario -> covenção em python p nome composto
print(nome)

media = 0

# criar variaveis ao mesmo tempo
# mesmo tipo:
n1 = n2 = n3 = n4 = 0.0
# tipos diferentes:
nome, idade = 'Suely', 43

estado = True

# função type() -> mostra o tipo da variavel
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j))

# função isinstance() -> retorna true ou false se a variavel é do tipo informado
a = 10
b = 'Sol'
print(isinstance(a, int))
print(isinstance(b, str))
print(isinstance(a, (int, float)))

a = 40
c = 3
r = a*c
print(r)