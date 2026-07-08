def calculadora(x1,sinal,x2):
    calc = 0
    if sinal == '+':
        calc = x1 + x2
    elif sinal == '-':
        calc = x1 - x2
    elif sinal == '*':
        calc = x1 * x2
    elif sinal == '/':
        calc = x1 / x2
    return calc
n1 = float(input('Qual numero deseja inserir? '))
simbolos = input('Qual numero sinal inserir? ')
n2 = float(input('Qual numero deseja inserir? '))
print (calculadora(n1,simbolos,n2))