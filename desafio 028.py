numero=int(input('Qual o número que pensei de 1 até 5: '))
import random
n=random.randint(1,5)

print('O número escolhido é {}'. format(n))
if n==numero:
    print('Você acertou')
else:
    print('Você errou')

