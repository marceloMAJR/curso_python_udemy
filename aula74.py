"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


fala_bom_dia = criar_saudacao('Bom dia')
fala_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(fala_bom_dia(nome))
    print(fala_boa_noite(nome))