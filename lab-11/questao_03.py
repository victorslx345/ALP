import random
import time
while True:
    jogar = input('Voce deseja fazer uma pergunta? (sim/nao) ' )
    if jogar == 'nao':
        break
    elif jogar == 'sim':
        pergunta = input('Faça uma pergunta de sim ou não: ')
        chance = random.randint(1,10)
        print ('Hmmm....')
        time.sleep(2)
        print ('Estou quase...')
        time.sleep(3)
        if chance >5 :
            print ('não')
        else:
            print ('sim')
