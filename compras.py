from itens import Itens

animais = Itens()

class Compras:

    def opcoesProdutos():

        animais.item("./estoque/estoqueProdutos.csv")


    def opcoesAnimais():

        while True:
            
            escolhaAnimal = int(input("\nO que deseja comprar?\n1.Cachorro\n2.Gato\n3.Pássaro.\n4.Voltar\n"))

            if(escolhaAnimal == 1):
                animais.item("./estoque/estoqueCaes.csv")
                break

            elif(escolhaAnimal == 2):
                animais.item("./estoque/estoqueGatos.csv")
                break
            
            elif(escolhaAnimal == 3):
                animais.item("./estoque/estoquePassaros.csv")
                break
            
            elif(escolhaAnimal == 4):

                from layouts import opcoesMenuInicial
                opcoesMenuInicial()
                break

            else:
                print("\nOpção inválida!")

    
