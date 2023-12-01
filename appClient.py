from usuario import user
from layouts import opcoesMenuInicial


while True:  
    escolha = int(input("1.Login\n2.Cadastro\n"))
    usuario = user()
    
    if(escolha == 1):
        usuario.login()

    elif(escolha == 2):
        usuario.cadastrar()

    if(usuario.cadastrado):
        break
    
opcoesMenuInicial()



