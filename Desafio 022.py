# strip remove espaços colocados no início e fim
nome=str(input('Qual seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome))
# Retirar os espaços count(' ')
print(len(nome) - nome.count(' '))
lista=nome.split()
print(lista)
print(len(lista[0]))
