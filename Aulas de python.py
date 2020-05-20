# ordem de precedência nas operações
# ()
# **
# *, /, //, %
#  +, -

# \n para pular linhas no print

# {:>20} {:<20} {:^20} alinhamentos

print('_'*50)

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

n1=int(input('Digite um número: '))
print('Os numeros antes do {} são {} e {}'.format(n1, n1-1, n1+1))
print('\n O dobro de {} \n é {}, \n o triplo é {}, \n a raiz quadrada é {:.2f}'.format(n1, n1*2, n1*3, n1**(1/2)))

medida=int(input('digite uma medida em metros: '))
print('{} metros é igual a \n {}cm \n {}mm '.format(medida, medida*100, medida*1000))

print('A tabuda de {} é:'.format(medida))
print('-'*12)
print('{:2} x {} = {}'.format(1, medida, medida*1))
print('{:2} x {} = {}'.format(2, medida, medida*2))
print('{:2} x {} = {}'.format(3, medida, medida*3))
print('{:2} x {} = {}'.format(4, medida, medida*4))
print('{:2} x {} = {}'.format(5, medida, medida*5))
print('{:2} x {} = {}'.format(6, medida, medida*6))
print('{:2} x {} = {}'.format(7, medida, medida*7))
print('{:2} x {} = {}'.format(8, medida, medida*8))
print('{:2} x {} = {}'.format(9, medida, medida*9))
print('{:2} x {} = {}'.format(10, medida, medida*10))
print('-'*12)

money=float(input('Quantos dinheiro vc tem:R$ '))
print('Você pode comprar Us${:.2f} com {}'.format(money/5.85, money))
print('Com o desconto de 5% vc tem {:.2f}'.format(money*.95))
print('Com +15% vc tem {:.2f}'.format(money*1.15))

comp=int(input('Qual a comprimento: '))
larg=int(input('Qual a largura: '))
area=comp*larg
print('Para pintar {:.2f} m2 vc precisa de: {:.2f} litos de tinta '.format(area, area/3))

tempC=float(input('Digite uma temperatura em C:'))
print('A temperatura em F de {}C é {:.2f}F'.format(tempC, (1.8*tempC)+32))

alugueldias=int(input('Quantos dias vc alugou o carro? (dias)'))
aluguelkm=float(input('Quantos km você rodou? (km)'))
custo=(alugueldias*60)+(aluguelkm*.15)
print('O custo do seu aluguel de {}dias e {:.2f}km rodados é de US${:.2f}'.format(alugueldias, aluguelkm, custo))

print('_'*50)

# Aula 00 #