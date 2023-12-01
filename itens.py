import csv
from receita import receita
Receita = receita()


class Itens:
    
    def __init__(self):
        self.listaItens = [] * 100
        self.receita = [] * 10

    def pegarProduto(self, num, animal):
         
        if(num > len(self.listaItens) or num <= 0):
            print("\nOpção Inválida!\n")
            from layouts import Layouts
            Layouts.opcoesMenuInicial()
            return

        animalSelecionado = self.listaItens[num-1]

        if(int(animalSelecionado[2]) <= 0):
            from layouts import Layouts
            print("\nITEM ESGOTADO!\n")
            self.listaItens.clear()
            Layouts.opcoesMenuInicial()
            return

        else: 

            animalSelecionado[2] = int(animalSelecionado[2]) - 1

            with open(animal, "w", encoding="utf-8") as arquivo:       
                for i in self.listaItens:
                    linha = str(i).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
                    arquivo.write(f"{linha}\n")
            
            self.listaItens.clear()

            print("\nITEM COMPRADO COM SUCESSO!\n")

            Receita.ganhos(int(animalSelecionado[1])) 

            from layouts import Layouts   

            Layouts.opcoesMenuInicial()


    def item(self, animal):
        self.listaItens.clear()
        print("\nO que deseja comprar?\n")

        with open(animal, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")

            for i, linha in enumerate(arquivo_csv):
                self.listaItens.append(linha)
                print(f"\n{i+1}.\nRaça: {linha[0]}\nValor: R${linha[1]}\n")  
            
            escolhaAnimal = int(input())

            self.pegarProduto(escolhaAnimal, animal)



    
  
    

          
            
        

    

    

