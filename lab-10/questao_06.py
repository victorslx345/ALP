num = int(input('Escolha um numero para ver a tabuada (1-10): '))
while num < 1 or num > 10:
    num = int(input('Escolha um numero para ver a tabuada (1-10): '))
for cont in range (1,11):
    print (f'{num} X {cont} =', num*cont)