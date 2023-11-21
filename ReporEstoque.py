import csv


class ReporEstoque:

    def __init__(self):
        self.listaEstoque = [] * 100
        self.nomeNovoItem = ''
        self.valorNovoItem = ''
        self.quantidadeNovoItem = ''

    def Gastos():
        print("aqui os gastos serão calculados")

    def exclusaoItemEstoque():
        print("")

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

        with open(estoque, "a", encoding="utf8") as arquivo:
            arquivo.write(f"\n{self.nomeNovoItem},{self.valorNovoItem},{self.quantidadeNovoItem}")


    def animalSelecionado(self, animalSelecionado, caminho):
        
        quantidade = int(input("Digite a quantidade que será adicionada ao item:\n"))
        novaQuantidade = quantidade + int(self.listaEstoque[animalSelecionado-1][2])

        self.listaEstoque[animalSelecionado-1][2] = str(novaQuantidade )

        with open(caminho, "w", encoding="utf-8") as arquivo:       
            for i in self.listaEstoque:
                linha = str(i).replace("'", "").replace("[", "").replace("]", "").replace(" ", "")

                arquivo.write(f"{linha}\n")
        


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

                itemAdicionado = int( input("Você irá adicionar um novo:\n1.Cachorro\n2.Gato\n3.Pássaro\n4.Produto\n5.Sair"))

                if(itemAdicionado > 5 | itemAdicionado < 1):
                    return print("Opção inválida!")

                else:
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
                print("excluindo aqui...")