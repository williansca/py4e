# elevator exercise

input = input('Pressione o andar desejado: ')
input = int(input)
primeiroAndar = 1;
ultimoAndar = 6;
try:
    if (input >= primeiroAndar) and (input <= 6):
        if input == 1:
            print('Primeiro andar')
        elif input == 2:
            print('Segundo andar')
        elif input == 3:
            print('Terceiro andar')
        elif input == 4:
            print('Quarto andar')
        elif input == 5:
            print('Quinto andar')
        elif input == 6:
            print('Cobertura')
except:
    input = -1
if (input >= primeiroAndar) and (input <= 6):
    print('Você chegou ao andar desejado')
else:
    print('Não é um andar válido')



