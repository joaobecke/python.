"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input("Digite um numero: ")

if num_str.isdigit():
    num_int = int(num_str)
    rest_div = num_int % 2
    if rest_div == 0:
     print ("O numero que você digitou é par")
    else:
        print('O numero que você digitou é impar')
else:
    print('Digite apenas numeros inteiros')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input ('Digite a hora do dia: ')

if hora_str.isdigit():
    hora_int = int(hora_str)
    if hora_int <= 11:
        print('Bom dia!')
    elif hora_int <= 17:
        print('Boa Tarde!') 
    else:
        print('Boa noite!')
else:
    print('Você nao digitou um horario.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print('Seu nome é curto demais')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande demais')
