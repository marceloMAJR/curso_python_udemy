"""
Introdução ao desempacotamento
"""
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# _, nome2, *_ = ['Maria', 'Helena', 'Luiz']
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)