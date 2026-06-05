maior = float('-inf')
# o valor tem que ser MENOS inf
controle = 1
while controle <= 10:
    # o variavel de controle soma nao existe
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    controle += 1
    # o valor da variavel de controle nao muda2
print('O maior número é', maior)
