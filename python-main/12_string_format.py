a = 'A'
b = 'B'
c = 1.1
formato = 'a={0} a={1} b={1} c={nome3:.2f}' .format(a , b, nome3=c)

print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))