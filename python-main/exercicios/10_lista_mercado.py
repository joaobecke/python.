import os

lista = [ ]


while True:
    print('Selecione uma opção.')
    opcao = input ('[i]nserir, [l]istar, [a]pagar: ')
   
    if opcao == 'i':
        os.system('cls')
        produto = input('Produto: ')
        lista.append(produto)
    elif opcao == 'a':
        indice_str = input ('Escolhe o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print ('Não a nada para listar!')

        for i , valor in enumerate(lista):
            print (i, valor)
    else:
        print (' Por favor, escolha i , a ou l!')