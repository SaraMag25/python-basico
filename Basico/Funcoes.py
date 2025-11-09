def somar(a, b):
    resultado = a + b
    return resultado
print(somar(1, 2))

def envia_email():
    email = 'naoexiste@gmail.com',
    senha = '1234'
    email_envio = 'outroteste@gmail.com'

#exemplo de como usar uma funcao que nao retorna nada
pessoas = ['Sara', 'Fabricio', 'Clara', 'Maria']
for p in pessoas:
    envia_email()

pessoas_2 = [
    {'nome' : 'Sara',
     'email': 'naoexiste@gmail.com'
    },
    {'nome' : 'Clara',
     'email': 'naoexisteClara@gmail.com'
    }
]

#mostra o nome e o email da pessoa

def envia_email_2(nome, email):
    nome_dest = nome
    email_envio = email
    return f'Email enviado para {nome}, dono do email {email}'


for p in pessoas_2:
    email_enviado = envia_email_2(p['nome'], p['email'])
    print(email_enviado)