from itens import Itens

animais = Itens()

class Compras:

    def opcoesProdutos():

        animais.item("estoqueProdutos.csv")


    def opcoesAnimais():

        while True:
            
            escolhaAnimal = int(input("O que deseja comprar?\n1.Cachorro\n2.Gato\n3.Pássaro.\n4.Voltar\n"))

            if(escolhaAnimal == 1):
                animais.item("estoqueCaes.csv")
                break

            elif(escolhaAnimal == 2):
                animais.item("estoqueGatos.csv")
                break
            
            elif(escolhaAnimal == 3):
                animais.item("estoquePassaros.csv")
                break
            
            elif(escolhaAnimal == 4):

                from layouts import Layouts
                Layouts.opcoesMenuInicial()
                break

            else:
                print("\nOpção inválida!")

    
