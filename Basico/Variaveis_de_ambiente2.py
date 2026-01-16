import Variaveis_de_ambientes
import os
usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')
 
login = Variaveis_de_ambientes.login(usuario, senha)
print(login)