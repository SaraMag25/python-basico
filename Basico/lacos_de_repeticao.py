def envia_email(i,cliente):
    print(f'{i} o email foi enviado ao cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Sara', 'Felipe', 'Rute']

for i,cliente in enumerate (clientes):
    if i == 2:
        break
    envia_email(i, cliente)

numero = 0
while numero < 5:
    if numero == 2:
        break
    print(numero)
    numero += 1


for i,cliente in enumerate (clientes):
    if i == 2:
        continue
    envia_email(i, cliente)
