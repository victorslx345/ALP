print ('JOGO DAS ESCADAS')
#HAPPY BIRTHDAY DANIEL
degrau = 1
print ('======REGRAS======')
print ('múltiplo de 3 (n % 3 == 0): Volte 1 degrau')
print('múltiplo de 5 (n % 5 == 0): Avance mais 1 degrau')
print('múltiplo de 7 (n % 7 == 0): Avance mais 4 degraus!')
print('múltiplo de 11 (n % 11 == 0): Volte para o início')
while True:
    print ('Degrau atual:', degrau)
    passos = int(input('Quantos passos serão dados? (1-6) ou 0 para desistir '))
    print ('')
    if passos == 0:
        print ('Voce disistiu')
        break
    if passos < 1 or passos > 6:
        print ('O numero de passos esta fora dos limites')
        print ('')
        continue
    degrau += passos
    print ('')
    if degrau % 3 == 0:
        degrau -= 1
        print ('Volte 1 degrau')
    elif degrau % 5 == 0:
        degrau += 1
        print ('Avance 1 degrau')
    elif degrau % 7 == 0:
        degrau += 4
        print ('Avance 4 degraus')
    elif degrau % 11 == 0:
        degrau = 1
        print ('Volte ao inicio')
    print ('')
    if degrau >= 100:
        print ('PARABENS')
        print('Voce ganhou')
    
