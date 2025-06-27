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


import json
resp = {
          "children": [
            {
              "name": "E-Farsas",
              "type": "url",
              "url": "https://www.e-farsas.com/"
            },
            {
              "name": "G1 Fato ou Fake",
              "type": "url",
              "url": "https://g1.globo.com/fato-ou-fake/"
            },
            {
              "name": "Boatos.Org",
              "type": "url",
              "url": "https://www.boatos.org/"
            },
            {
              "name": "Estadão Verifica",
              "type": "url",
              "url": "https://politica.estadao.com.br/blogs/estadao-verifica/"
            },
            {
              "name": "Aos Fatos",
              "type": "url",
              "url": "https://www.aosfatos.org/"
            },
            {
              "name": "Lupa",
              "type": "url",
              "url": "https://piaui.folha.uol.com.br/lupa/"
            },
            {
              "name": "Comprova",
              "type": "url",
              "url": "https://noticias.uol.com.br/comprova/"
            },
            {
              "name": "O Truco",
              "type": "url",
              "url": "https://apublica.org/checagem/"
            }
          ],
          "name": "Checagem de Fake News",
          "type": "folder"
        }

print('===========')

first = json.dumps(resp)
lista = list(resp.keys())
print(lista)
x = lista[0]
print(x)
print(type(resp))