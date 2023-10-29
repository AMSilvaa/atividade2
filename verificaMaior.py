print('DIGITE 3 VALORES INTEIROS')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

menor = x

if y < menor:
    menor = y


if z < menor:
    menor = z


print("O menor número é:", menor)

  