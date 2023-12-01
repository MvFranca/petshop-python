import csv
from receita import receita
Receita = receita()

class ReporEstoque:

    def __init__(self):
        self.listaEstoque = [] * 100
        self.nomeNovoItem = ''
        self.valorNovoItem = ''
        self.custo = ''
        self.quantidadeNovoItem = ''
        self.receita = [] * 10

    def exclusaoItemEstoque(self, estoque):
        
        with open(estoque, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")

            for i, linha in enumerate(arquivo_csv):
                self.listaEstoque.append(linha)
                print(f"\n{i+1}.\nRaça: {linha[0]}\nValor: R${linha[1]}\nQuantidade: {linha[2]}\n") 


        escolhaExclusao = int(input("\nDigite o número do item que será excluído: \n"))

        self.listaEstoque.pop(escolhaExclusao-1)

        with open(estoque, "w", encoding="utf8") as arquivo: 
            for i in self.listaEstoque: 
                arquivo.write(f"{i[0]},{i[1]},{i[2]}\n")

        self.listaEstoque.clear()


    def adicionarItemEstoque(self, escolha):

        if(escolha == 1):
            estoque = "./estoque/estoqueCaes.csv"
        elif(escolha == 2):
            estoque = "./estoque/estoqueGatos.csv"
        elif(escolha == 3):
            estoque = "./estoque/estoquePassaros.csv"
        elif(escolha == 4):
            estoque = "./estoque/estoqueProdutos.csv"

        self.nomeNovoItem = input("\nDigite o nome/raça do item que será adicionado:\n ")
        self.valorNovoItem = input(f"\nDigite o preço de venda d@ {self.nomeNovoItem}: \n")
        self.custo = input(f"\nDigite o custo de compra d@ {self.nomeNovoItem}: \n")
        self.quantidadeNovoItem = input(f"\nDigite a quantidade que será adicionada ao estoque: \n")

        novoItem = f"{self.nomeNovoItem},{self.valorNovoItem},{self.quantidadeNovoItem}\n"
        
        with open(estoque, "a", encoding="utf-8") as arquivo:
            arquivo.write(novoItem)  

        gasto = round((int(self.custo)) * int(self.quantidadeNovoItem))
        Receita.gastos(gasto)
        self.listaEstoque.clear()
        self.escolhaReposicao()


    def animalSelecionado(self, animalSelecionado, caminho):
        
        quantidade = int(input("Digite a quantidade que será adicionada ao item:\n"))
        novaQuantidade = quantidade + int(self.listaEstoque[animalSelecionado-1][2])

        gasto = round((int(self.listaEstoque[animalSelecionado-1][1])/2) * quantidade)

        Receita.gastos(gasto)


        self.listaEstoque[animalSelecionado-1][2] = str(novaQuantidade )

        with open(caminho, "w", encoding="utf-8") as arquivo:       
            for i in self.listaEstoque:
                linha = str(i).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")

                arquivo.write(f"{linha}\n")
        self.listaEstoque.clear()
        

    def reposicaoAnimal(self, item, tipo):

        print("\nQual item deseja repor?\n")
        
        with open(item, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")

            for i, linha in enumerate(arquivo_csv):
                self.listaEstoque.append(linha)

                if(tipo == 'a'):
                    print(f"\n{i+1}.\nRaça: {linha[0]}\nQuantidade: {linha[2]}\nCusto: R${int(linha[1])/2}\n") 
                elif(tipo == 'p'):
                    print(f"\n{i+1}.\nProduto: {linha[0]}\nQuantidade: {linha[2]}\nCusto: R${int(linha[1])/2}\n") 

            itemSelecionado = int(input())
            
            if(itemSelecionado > len(self.listaEstoque) or itemSelecionado <= 0):
                print("\nOpção Inválida!\n")
                self.listaEstoque.clear()
                self.escolhaReposicao()
                return
            else:
                self.animalSelecionado(itemSelecionado, item)

    def escolhaReposicao(self):
        
       from layoutsBack import escolhaReposicao
       escolhaReposicao.opcoesMenu()