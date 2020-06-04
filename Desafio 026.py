texto=str(input('Digite uma frase'))
print('A letra A aparece {} vezes'.format(texto.upper().count('A')))
print('A letra A apareceu pela primiera vez na posição {}'. format((texto.upper().find("A"))))
print('A última ocorrência de A foi {}'.format(texto.upper().rfind('A')))