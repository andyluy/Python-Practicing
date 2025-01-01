bananas = int(input('Digite a quantidade de bananas vendidas: '))
macas = int(input('Digite a quantidade de maças vendidas: '))

if bananas > macas:
    print('As bananas tiveram mais vendas')
elif macas > bananas:
    print('As maças tiveram mais vendas')
else:
    print('Bananas e maças tiveram a mesma quantidade de vendas')
