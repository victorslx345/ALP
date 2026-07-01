import random
n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
for tentativa in range(1,11):
    r1 = int(input(''))
    r2 = int(input(''))
    r3 = int(input(''))
    s1 = '_'
    s2 = '_'
    s3 = '_'
    if r1 == n1:
        s1 = '+'
    elif r1 == n2 or r1 == n3:
        s1 = "!"
    else:
        s1 = "_"
    if r2 == n2:
        s2 = '+'
    elif r2 == n1 or r2 == n3:
        s2 = "!"
    else:
        s2 = "_"
    if r3 == n3:
        s3 = '+'
    elif r3 == n1 or r3 == n2:
        s3 = "!"
    else:
        s3 = "_"
    print (f'\n{r1} {r2} {r3}')
    print (f'{s1} {s2} {s3}\n')
    if s1 == "+" and s2 == '+' and s3 == '+':
        print('Voce ganhou!')
        break
    print(f'Tentativas restantes: {10 - tentativa}\n')