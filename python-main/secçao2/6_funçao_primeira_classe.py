# Higher Order Functions 
# Funçoes de primeira classe

def saudacao(msg, nome):
    return f'{msg} , f{nome}'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia')
print(v) 