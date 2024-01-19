"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Joao'
preco = 100.9589
variavel = '%s , o  total foi R$%.2f' % ( nome, preco)
print(variavel)