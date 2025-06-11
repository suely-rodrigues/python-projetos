#Simples, Composto, Encadeado


n1 =n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#calcular a media aritmetica:
media = (n1+n2)/2

#bloco condicional
if (media>=7):
    print('Resultado: Aprovado!')
    print('Parabéns!')
elif (media>=5):
    print('Você está de recuperação.')
else:
    print('Aluno reprovado...')

#fora do bloco8
print('Sua média é {}'.format(media))