frase = 'O python é uma linguagem de programaçãomultiparadigma. python fpo criado por Guido van Rossum.'

i = 0 
mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    contador = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1 
        continue

    if mais_vezes < contador :
        mais_vezes = contador
        letra_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi'
f'{letra_mais_vezes} que apareceu '
f'{mais_vezes} x')

