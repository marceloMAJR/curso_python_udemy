"""
Iterando strings com while
"""
#     0123456789

nome = 'Marcelo Martins'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]+"*"
    novo_nome += letra
    indice += 1

print(novo_nome)