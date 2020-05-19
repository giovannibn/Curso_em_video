# AULA 007 #
nome=str(input('Qual seu nome? '))
print('Olá {:<20}'.format(nome))
print('Olá {:>20}'.format(nome))
print('Olá {:^20}'.format(nome))
print('Olá {:*^20}'.format(nome))

n1=int(input('Digite n1: '))
n2=int(input('Digite n2: '))
s=n1+n2
p=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
m=(n1+n2)/2
print('A soma é {}, \n o produto é {}, \na divisão é {:.4f}, \n a potencia é {}, \n a Div Inteira é {:.4f}, \n a média é {}'.format(s, p, d, p, di, m))

n3=int(input('Digite um número: '))
print('Os numeros antes do {} são {} e {}'.format(n3, n3-1, n3+1))
print('\n O dobro de {} \n é {}, \n o triplo é {}, \n a raiz quadrada é {}'.format(n3, n3*2, n3*3, n3**(1/2)))

medida=int(input('digite uma medida em metros: '))
print('{} metros é igual a \n {}cm \n {}mm '.format(medida, medida*100, medida*1000))

print('A tabuda de {} é:\n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{}, \n{} '.format(medida, medida*1, medida*2, medida*3,medida*4, medida*5, medida*6, medida*7, medida*8, medida*9, medida*10))

money=int(input('Quantos dinheiro vc tem: '))
print('Você pode comprar {} dolares com {}'.format(money/5.85, money))
print('Com o desconto de 5% vc tem {}'.format(money*.95))
print('Com +15% vc tem {}'.format(money*1.15))

comp=int(input('Qual a comprimento: '))
larg=int(input('Qual a largura: '))
area=comp*larg
print('Para pintar {} m2 vc precisa de: {} litos de tinta '.format(area, area/3))

# Aula 008 #