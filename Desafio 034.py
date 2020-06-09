salario=float(input('Digite seu salário'))
if salario<=1250:
    print('Seu salário com aumento será de R$ {}'.format(salario*1.15))
else:
    print('Seu salário com aumento será de R$ {}'.format(salario*1.1))