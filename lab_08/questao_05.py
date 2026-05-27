conta = 0
while True:
    print ('Cardapio')
    print ('1.Pão de Queijo - 3,65R$')
    print ('2.All mosso - 14,60R$')
    print ('3.Suco - 2,00R$')
    print ('4.Coxinha - 7,00R$')
    print ('5.Fechar Menu')
    print('')
    PQ =3.65
    AL = 14.60
    SUCO = 2
    COX = 7
    
    choose = int(input('Escolha algo do cardapio: '))
    print ('')
    if choose == 1:
        conta+=PQ
    elif choose==2:
        conta+=AL
    elif choose==3:
        conta+=SUCO
    elif choose==4:
        conta+=COX
    elif choose==5:
        print ('A conta deu', conta)
        break