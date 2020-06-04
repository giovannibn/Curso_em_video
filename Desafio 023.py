num=int(input('Digite um número de 0 até 9999:'))
unidade=num%10
dezena=num//10%10
centena=num//100%10
milhar=num//1000%10
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))
