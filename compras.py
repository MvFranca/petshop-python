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

            if(escolhaAnimal == 2):
                animais.item("estoqueGatos.csv")
                break
            
            if(escolhaAnimal == 3):
                animais.item("estoquePassaros.csv")
                break

            else:
                print("\nOpção inválida!")

    
