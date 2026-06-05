import random # essa deve ser a primeira linha do código

num = (random.randint(1, 10))
chance = 4
while chance > 0:
    tentativa = int(input(f'Acerte o numero que estou pensando, voce tem {chance} tenatativas: '))
    chance -=1
    if tentativa == num:
        print ('Parabens voce acertou!')
        break
    else:
        if tentativa < num:
            print('O numero é maior que', tentativa)
        else:
            print('O numero é menor que', tentativa)
if chance <= 0:
    print ('Acabou as tentativas')