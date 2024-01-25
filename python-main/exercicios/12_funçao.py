# Exercicios com funçoes 

# Crie uma funçao que mutipplica todos os argumentos 
# nao nomeados recebidos 
# Retorne o total para uma variavel e mostre o valor 
# da variavel 

# Crie uma funçao fala se um numero é par ou impar.
# Retorne se o numero é par ou impar.

numero = input(print('Digite um numero? '))
outro_numero = input(print('Digite outro numero? '))

int_numero_1 =  int(numero)
int_numero_2 =  int(outro_numero)

resultado = int_numero_1 * int_numero_2

print(resultado)


if resultado % 2 == 0: 
    print('Este resultado é par!')
else:
    print("Este resultado é impar!")



