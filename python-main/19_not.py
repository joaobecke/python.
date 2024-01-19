# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha_correta = '12345'
senha = input('Senha; ')

if not senha:
    print('Você nao digitou nada!')
elif senha_correta == senha:
    print('entrou no sistema!')

else:
    print('Você digitou a senha errada')

print(not True) #false
print(not False) #true