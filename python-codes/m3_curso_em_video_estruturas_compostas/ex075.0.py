val = ()
valpar = ()
for c in range(0,4):
    val += (int(input('Digite um número: ')),)
print(f'\nVocê digitou os valores {val}')
print(f'O valor 9 apareceu {val.count(9)} vezes.')
if 3 in val:
    print(f'Posição do primeiro 3 digitado: {val.index(3)+1}')
else:
    print('Nenhum 3 foi digitado.')
for c in val:
    if c % 2 == 0:
        valpar += c,
if valpar == ():
    print('Nenhum número par foi digitado.')
else:
    print(f'Os números pares foram: {valpar}')