import random

def rock_paper_scissors():
    opcoes = ['pedra', 'papel', 'tesoura']
    usuario = input('Escolha: pedra, papel ou tesoura. ')
    computador = random.choice(opcoes)
    if not (usuario in opcoes):
        return 'Entrada incorreta'
    elif usuario == computador:
        return f'Empate, o computador também escolheu {computador}'
    elif (usuario == 'pedra' and computador == 'tesoura') or (usuario == 'papel' and computador == 'pedra') or (usuario == 'tesoura' and computador == 'papel'):
        return f'Vitoria, o computador escolheu {computador}'
    else:
        return f'Derrota, o computador escolheu {computador}'
    
    
saida = rock_paper_scissors()
print(saida)