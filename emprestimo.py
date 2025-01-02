renda = int(input('Digite o valor da sua renda mensal: '))
parcela = int(input('Digite o valor da parcela desejada: '))
if renda*0.3 < parcela:
    print('Empréstimo negado: Parcela acima de 30% da renda. ')
else: 
    print('Empréstimo aprovado!')