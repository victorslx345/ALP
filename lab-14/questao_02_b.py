def ola(nome,genero):
    if genero == 'masculino':
        return f'Ola {nome}, Bem vindo!'
    elif genero == 'feminino':
        return f'Ola {nome}, Bem vinda!'
    else:
        return f'Ola {nome}, Boas vindas!'
Nome = input('Qual o seu nome?')
Genero = input('Qual o seu genero? ')
print(ola(Nome,Genero))