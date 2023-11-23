import csv


class ReporEstoque:

    def __init__(self):
        self.listaEstoque = [] * 100
        self.nomeNovoItem = ''
        self.valorNovoItem = ''
        self.quantidadeNovoItem = ''
        self.receita = [] * 10

    def gastos(self, valor): 
        with open("receita.csv", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 
            valores = i.replace("\n", "") 
            self.receita.append(valores)  

        for i in self.receita:
            ganhos, gastos, lucro = i.split(",")
        

        atualizacao = f"{ganhos},{int(gastos) + valor},{int(ganhos) - (int(gastos) + valor)}"
        
        with open("receita.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{atualizacao}\n")

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
            estoque = "estoqueCaes.csv"
        elif(escolha == 2):
            estoque = "estoqueGatos.csv"
        elif(escolha == 3):
            estoque = "estoquePassaros.csv"
        elif(escolha == 4):
            estoque = "estoqueProdutos.csv"

        self.nomeNovoItem = input("Digite o nome/raça do item que será adicionado:\n ")
        self.valorNovoItem = input(f"Digite o valor d@ {self.nomeNovoItem}: \n")
        self.quantidadeNovoItem = input(f"Digite a quantidade que será adicionada ao estoque: \n")

        gasto = round((int(self.valorNovoItem)/2) * int(self.quantidadeNovoItem))
        self.gastos(gasto)


    def animalSelecionado(self, animalSelecionado, caminho):
        
        quantidade = int(input("Digite a quantidade que será adicionada ao item:\n"))
        novaQuantidade = quantidade + int(self.listaEstoque[animalSelecionado-1][2])

        gasto = round((int(self.listaEstoque[animalSelecionado-1][1])/2) * quantidade)

        self.gastos(gasto)


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
                    print(f"\n{i+1}.\nRaça: {linha[0]}\nQuantidade: {linha[2]}\n") 
                elif(tipo == 'p'):
                    print(f"\n{i+1}.\nProduto: {linha[0]}\nQuantidade: {linha[2]}\n") 

            itemSelecionado = int(input())
            self.animalSelecionado(itemSelecionado, item)



    def escolhaReposicao(self):
        
        while True:

            escolhaServer = int(input("\nO que deseja fazer?\n1.Adicionar um novo item ao estoque\n2.Atualizar quantidade de um item\n3.Excluir item do estoque\n"))

            if(escolhaServer == 1):


                itemAdicionado = int( input("Você irá adicionar um novo:\n1.Cachorro\n2.Gato\n3.Pássaro\n4.Produto\n5.Sair\n"))

                if(itemAdicionado > 5 or itemAdicionado < 1):
                    print("\nOpção inválida!\n")
                    return self.escolhaReposicao() 

                self.adicionarItemEstoque(itemAdicionado)
                break

            elif(escolhaServer == 2):
                escolhaReposicao = int(input("Reponha o estoque de um dos seguintes recursos:\n1.Animais\n2.Produtos\n"))

                if(escolhaReposicao == 1):

                    reposicaoAnimais = int(input("Reponha o estoque de um dos seguintes animais:\n1.Cães\n2.Gatos\n3.Pássaros\n"))

                    if(reposicaoAnimais == 1):
                        self.reposicaoAnimal("estoqueCaes.csv", 'a')
                    elif(reposicaoAnimais == 2):
                        self.reposicaoAnimal("estoqueGatos.csv", 'a')
                    elif(reposicaoAnimais == 3):
                        self.reposicaoAnimal("estoquePassaros.csv", 'a')

                elif(escolhaReposicao == 2):
                    self.reposicaoAnimal("estoqueProdutos.csv", 'p')
                break

            elif(escolhaServer == 3):

                while True:
                    
                    excluirItem = int(input("\nEscolha a categoria do item que será excluído:\n1.Cães\n2.Gatos\n3.Pássaros\n4.Produtos"))

                    if(excluirItem == 1):
                            self.exclusaoItemEstoque("estoqueCaes.csv")
                            break
                    elif(excluirItem == 2):
                        self.exclusaoItemEstoque("estoqueGatos.csv")
                        break
                    elif(excluirItem == 3):
                        self.exclusaoItemEstoque("estoquePassaros.csv")
                        break
                    elif(excluirItem == 4):
                        self.exclusaoItemEstoque("estoqueProdutos.csv")
                        break  
                        
                            


