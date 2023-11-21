from usuario import user
from layouts import Layouts

usuario = user()

while True:  

    usuario.cadastrar()
    if(usuario.cadastrado):
        break
    
Layouts.opcoesMenuInicial()



