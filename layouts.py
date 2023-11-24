from compras import Compras

compras = Compras

class Layouts:

    def opcoesMenuInicial():    

        while True:

            menuInitial = int(input("\nO que você deseja fazer? \n1. Comprar um pet.\n2.Comprar um produto para o meu pet.\n3.Serviços para o pet.\n4. Sair\n"))
            
            if(menuInitial == 1):
                compras.opcoesAnimais()
                break
            
            elif(menuInitial == 2):
                compras.opcoesProdutos()
                break

            elif(menuInitial == 3):
                print("Função indisponível no momento!\n")

            elif(menuInitial == 4):
                break
