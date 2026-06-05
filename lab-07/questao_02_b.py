soma = 0
controle = 1
# a variavel soma nao podia ser a variavel de controle
while controle <= 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
    controle += 1
print (soma)
# nao tinha o print para mostrar o resultado