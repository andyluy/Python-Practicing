primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota+segunda_nota+terceira_nota)/3
print(media)
if media > 7:
    print('Aprovado')
elif 4 <= media < 7:
    print('Recuperacao')
else:
    print('reprovado')