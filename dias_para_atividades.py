def informe_dias ():
    while True:
        dias = int(input('Informe os dias para a atividade: '))
        if dias >= 1:
            return dias
        else:
            print('Erro: os dias não podem ser negativos.')

A = informe_dias()
B = informe_dias()
C = informe_dias()

print('dias para a atividade ', A)
print('dias para a atividade ', B)
print('dias para a atividade ', C)