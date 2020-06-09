ano=int(input('Digite um ano: '))
div4=ano%4
ndiv100=ano%100
div400=ano%400
if (div4==0 and ndiv100!=0 or div400==0):
    print('Bissesto')
else:
    print('Não é bissesto')