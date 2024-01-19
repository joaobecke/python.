nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é', nome[-1:-10:-1] )
    print()

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
         print(f"Seu nome não contém espaço")

    print('Seu nome tem', len(nome), 'letras')
    print('A primeira letra do seu nome é', nome[0])
    print('A ultima letra do seu nome é', nome[-1])
else:
    print("Desculpe, você deixou campos vazios")
 

