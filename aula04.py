# n = input('Digite algo:')
# print('O tipo primitivo desse valor é', type(n))
# print('Só tem espaços?', (n.isspace()))
# print('É um número?', (n.isnumeric()))
# print('É alfabético?', (n.isalpha()))
# print('É alfanúmerico:', (n.isalnum()))
# print('Está em maiúsculas?', (n.isupper()))
# print('Está em minúsculas?', (n.islower()))
# print('Está capitalizada?', (n.istitle()))

n = input('Digite algo:')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaçõs? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanúmerico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizado? {}'.format(n.istitle()))
