saldo = 0
while True:  # loop infinito
    print('Cardápio')
    print('1. Açaí 300ml - R$ 12')
    print('2. Mousse - R$ 6,50')
    print('3. Salada de frutas - R$ 10')
    print('4. Fechar a conta')
    # copie do exemplo pq to com preguiça :D
    num = int(input('Faça o pedido: '))
    if num == 1:
        saldo += 12
    elif num == 2:
        saldo += 6.50
    elif num == 3:
        saldo += 10
    elif num == 4:
        print (F'A conta deu R${saldo}')
        break
