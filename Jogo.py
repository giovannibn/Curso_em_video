#import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#Gerar Apostas de Loterias
print("Escolha o tipo de aposta, 1-Mega Sena ou 2=Quina")
mega=sorted(random.sample(range(1,60),6))
quina=sorted(random.sample(range(1,80),6))
x=input(str())
if x=="1":
    print(mega)
elif x=="2":
    print(quina)
else:
    print("Escolha o tipo de aposta, 1-Mega Sena ou 2=Quina")


Mega=sorted(random.sample(range(1,60),6))
Mega