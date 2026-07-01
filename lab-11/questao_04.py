
import random
import time
pts1 = 0
pts2 = 0
dado = random.randint(1,6)
dado2 = random.randint(1,6)
rodada = 1
print('Eu vou rolar dois dados, quem chegar mais perto do numeros somados ganha')
while True:
    dado = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado + dado2
    time.sleep(1)
    print(f'========== RODADA {rodada} ==========')
    time.sleep(2)
    jogador1 = int(input(f'Jogador 1 (Pontos {pts1}) De um palíte: '))
    jogador2 = int(input(f'Jogador 2 (Pontos {pts2}) De um palíte: '))
    print ('🎲 Rolando os dados...')
    time.sleep(2)
    print(f'Dado 1: {dado}')
    print(f'Dado 2: {dado2}')
    if abs(soma - jogador1) < abs(soma - jogador2):
        pts1 += 5
        print ('Jogador 1 ganhou 5 pontos!!')
    elif abs(soma - jogador1) == abs(soma - jogador2):
        pts1 += 2
        pts2 += 2
        print ('EMPATE! Cada um ganha 2 pontos')
    else:
        pts2 += 5
        print ('Jogador 2 ganhou 5 pontos!!')
    if pts1 >= 50:
        print('JOGADOR 1 VENCEU!')
    elif pts2 >= 50:
        print('JOGADOR 2 VENCEU!')
    
    
    
