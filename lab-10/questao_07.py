win = 0
lose = 0
draw = 0
cont = int(input('Coloque a quantidade de jogos: '))
for jogos in range(cont):
    atl = int(input('Qual a quantidade de gols que o Atletico fez? '))
    inm = int(input('Qual a quantidade de gols que o time inimigo fez? '))
    if atl > inm:
        win += 1
    elif inm > atl:
        lose += 1
    else:
        draw += 1
print ('Vitorias :', win)
print('Empate :', draw)
print('Derrotas :', lose)
print('Pontução:', (win*3)+(lose*0)+(draw*1))
