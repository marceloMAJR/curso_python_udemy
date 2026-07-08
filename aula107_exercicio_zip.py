# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    return list(zip(lista1, lista2))

def zipper_longest(lista1, lista2, fillvalue='Sem Cidade'):
    return list(zip_longest(lista1, lista2, fillvalue=fillvalue))

lista_zipper = zipper(l1, l2)
print('Usando a função zip do Python')
print(lista_zipper)
print()

lista_zipper_longest = zipper_longest(l1, l2)
print('Usando a função zip_longest do Python')
print(lista_zipper_longest)
print()

# Outra possível solução usando list comprehension
def zipper2(l1,l2):
    intervalo_max = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo_max)]

print('Usando list comprehension')
print(zipper2(l1, l2))

# "from itertools import zip_longest" - para unir listas de tamanhos diferentes, preenchendo com None os valores faltantes