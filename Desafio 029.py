vel=float(input('Digite a velocidade: '))
if vel>80:
    print('Vcê ultrapassou a velocidade de 80km/h e foi multado em R${:.2f}'.format((vel-80)*7))
else:
    print('Tenha um bom dia e respeite os limite de velocidade')
