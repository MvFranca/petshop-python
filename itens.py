import csv

class Itens:
    
    def __init__(self):
        self.listaItens = [] * 100
        self.receita = [] * 10

    def ganhos(self, valor):
        with open("receita.csv", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 
            valores = i.replace("\n", "") 
            self.receita.append(valores)  


        for i in self.receita:
            ganhos, gastos, lucro = i.split(",")
        
        lucro = (int(ganhos) + valor) - int(gastos)
        atualizacao = f"{int(ganhos)+valor},{gastos},{lucro}"
        
        with open("receita.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{atualizacao}\n")



    def pegarProduto(self, num, animal):
        
        caoSelecionado = self.listaItens[num-1]

        caoSelecionado[2] = int(caoSelecionado[2]) - 1


        with open(animal, "w", encoding="utf-8") as arquivo:       
            for i in self.listaItens:
                linha = str(i).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
                arquivo.write(f"{linha}\n")
        
        self.listaItens.clear()

        print("\nITEM COMPRADO COM SUCESSO!\n")

        self.ganhos(int(caoSelecionado[1])) 

        from layouts import Layouts   

        Layouts.opcoesMenuInicial()


    def item(self, animal):

        print("\nO que deseja comprar?\n")

        with open(animal, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")

            for i, linha in enumerate(arquivo_csv):
                self.listaItens.append(linha)
                print(f"\n{i+1}.\nRaça: {linha[0]}\nValor: R${linha[1]}\n")  
            
            escolhaCachorro = int(input())
            self.pegarProduto(escolhaCachorro, animal)



    
  
    

          
            
        

    

    

