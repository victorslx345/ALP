def clsf(nota):
    if nota >= 60:
        print('APROVADO')
    else:
        print('REPROVADO')
nota = int(input('Qual foi sua nota? '))
clsf(nota)