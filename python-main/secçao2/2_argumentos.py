"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Refatorar: editar seu codigo.
"""

def soma(x, y, z=None):
    if z is not None:
     print(x + y + z)
    else:
        print (x + y)

soma(1, 2, 4)