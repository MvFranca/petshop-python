class user:
    def __init__(self):
       self.nomeDono = ''
       self.cpf = ''
       self.senha = ''
       self.idadeDono = ''
       self.celular = ''
       self.cidade = ''
       self.cadastrado = False

    def verificacao(self, userAdd):
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 

            i.replace("\n", "") 

            nome, cpf, idade, numero_telefone, cidade, senha = i.split(",")
            
            usuario = {
                "nome": nome,
                "cpf": cpf,
                "idade": idade,
                "numero_telefone": numero_telefone,
                "cidade": cidade,
                "senha": senha
            }

            if(self.cpf == usuario['cpf']):
                return print("Usuário já cadastrado!")

        
        self.cadastrado = True
        self.addClientes(userAdd)
        

    def addClientes(self, userAdd):       

        with open("clientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(userAdd)        
      

    def cadastrar(self):

        self.nomeDono = input("Digite seu nome: ")
        self.idade = input("Digite sua idade: ")
        self.cpf = input("Digite seu cpf: ")
        self.celular = input("Digite seu celular: ")
        self.cidade = input("Digite sua cidade: ")
        self.senha = input("Digite sua senha: ")

        userAdd = f"\n{self.nomeDono},{self.cpf},{self.idade},{self.celular},{self.cidade},{self.senha}"
        self.verificacao(userAdd)

    def login(self):
        
        self.cpf = input("Digite seu cpf:\n")
        self.senha = input("Digite sua senha:\n")

        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 

            i.replace("\n", "") 
            nome, cpf, idade, numero_telefone, cidade, senha = i.split(",")
            if(cpf == self.cpf and senha == self.senha):
                self.cadastrado = True
                break

        if(self.cadastrado == False):
            print("\nDados incorretos!\n")
        
        

    