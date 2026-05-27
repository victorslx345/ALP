cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
# quando o numero e par, o continue acontece, ignora o print e repete o loop; e quando impar o continue NAO acontece e o print roda