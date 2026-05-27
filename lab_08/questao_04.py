soma = 0
repetidor = 0
while repetidor == 0:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    if num % 2 != 0:
        continue
    soma += num
    print ('Soma atual:', soma)
    if soma >= 100:
        break