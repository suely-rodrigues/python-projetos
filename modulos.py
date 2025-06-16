import mod_func as mf
import numpy as np
import math
# from math import sqrt, sin  ->importa apenas as funções especificadas.
# from math import *  -> importa tudo do módulo e não precisa chamar math antes da função. import universal, não recomendado.
# import math as m -> importa math com alias m.

print(math.sqrt(81))

# controla fluxo de execução do codigo. __name__ variavel interna do Python com o nome do módulo atual. quando o modulo é executado como modulo principal, __name__ =='__main__', qndo é modulo importado __name__ recebe o nome do modulo. evita que partes do codigo sejam executadas na importação do modulo.
if __name__ == '__main__':
    mf.mensagem()

    num = int(input('Digite um numero inteiro: '))

    print(f'\nCalcular fatorial do numero: ')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')
    
    print(f'\nCalcular sequencia de fibonacci: ')
    fib = mf.fibo(num)
    print(f'A sequencia é {fib}')


L = np.array([1,2,3,4,5,6,7,8,9])
print(L)