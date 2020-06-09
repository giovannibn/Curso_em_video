dist=float(input('Qual a distancia da sua viagem em km? '))
if dist <= 200:
    print('O preço da sua passagem é de R$ {}'.format(dist*.50))
else:
    print(('O preço da sua passagem é de R$ {}'.format(dist*.45)))
