from usuario import user
from layouts import Layouts

usuario = user()

while True:  
    escolha = int(input("1.Login\n2.Cadastro\n"))

    if(escolha == 1):
        usuario.login()

    elif(escolha == 2):
        usuario.cadastrar()

    if(usuario.cadastrado):
        break
    
Layouts.opcoesMenuInicial()



