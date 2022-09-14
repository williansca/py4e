def comprimentar(opcao):
    if opcao == 'es':
        return 'Hola'
    elif opcao == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(comprimentar('en'), 'Carlos')

print(comprimentar('fr'), 'Kevin')

print(comprimentar('en'), 'Mary')
