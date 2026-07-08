import time
def contagem(x1):
    for i in range(x1,0,-1):
        print(i)
        time.sleep(1)
    print('Acabou o tempo')
tempo = abs(int(input('Em qual numero deseja começar a contagem regressiva? ')))
contagem(tempo)