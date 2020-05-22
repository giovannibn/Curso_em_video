import math
#num = float(input('Digite'))
#print(math.trunc(num))
#print(int(num))

#catop=float(input("digite o cateto oposto:"))
#catadj=float(input('Digite o catete adjacente'))
#print('A hioitenusa é:',math.hypot(catop, catadj))

# #from math import radians,sin, cos, tan (importando apenas as funções)
#angulo=float(input('Digite um angulo: (graus)'))
#print('O seno de {} é {:.2f}, o coseno é {:.2f}, a tangente é {:.2f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))

#019
import random
from random import sample
from random import shuffle
aluno1=str(input("Nome do aluno1:"))
aluno2=str(input('Nome do aluno2:'))
aluno3=str(input('Nome do aluno3:'))
aluno4=str(input('Nome do aluno4:'))
classe=[aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}'.format(random.choice(classe)))

#020
#print(('A ordem de apresentação é: {}'.format(sample(classe,4))))
random.shuffle(classe)
print('A ordem será: {}'.format(classe))

#21
#import pygame