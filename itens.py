import csv

class Itens:
    
    def __init__(self):
        self.listaItens = [] * 100


    def pegarProduto(self, num, animal):
        
        caoSelecionado = self.listaItens[num-1]

        caoSelecionado[2] = int(caoSelecionado[2]) - 1

        with open(animal, "w", encoding="utf-8") as arquivo:       
            for i in self.listaItens:
                linha = str(i).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
                arquivo.write(f"{linha}\n")
        
        self.listaItens.clear()

        print("\nITEM COMPRADO COM SUCESSO!\n")
            
        from layouts import Layouts   

        Layouts.opcoesMenuInicial()


    def item(self, animal):

        print("\nO que deseja comprar?\n")

        with open(animal, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")

            for i, linha in enumerate(arquivo_csv):
                self.listaItens.append(linha)
                print(f"\n{i+1}.\nRaça: {linha[0]}\nValor: R${linha[1]}\nQuantidade: {linha[2]}\n")  
            
            escolhaCachorro = int(input())
            self.pegarProduto(escolhaCachorro, animal)



    
  
    

          
            
        

    

    

