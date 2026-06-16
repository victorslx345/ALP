while True:
    print('Voce quer saber como fazer um ingenuo perder tempo?')
    resp = input('')
    if resp == 'n' or resp == 'N' or resp == 'nao' or resp == 'NAO' or resp == 'não' or resp == 'NÃO':
         break
    elif resp == 's' or resp == 'sim' or resp == 'SIM' or resp == 'S':
         continue
    else:
        print (f'"{resp}" não é uma resposta valida')
