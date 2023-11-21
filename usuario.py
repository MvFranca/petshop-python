class user:
    def __init__(self):
       
       self.nomeDono = ''
       self.cpf = ''
       self.idadeDono = ''
       self.celular = ''
       self.cidade = ''
       self.cadastrado = False

    def verificacao(self, userAdd):

        listaUsers = [] * 200

        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        

        for i in c: 
            cliente = i.replace("\n", "") 
            listaUsers.append(cliente)  

        for i in listaUsers:
            nome, cpf, idade, numero_telefone, cidade = i.split(",")
            
            usuario = {
                "nome": nome,
                "cpf": cpf,
                "idade": idade,
                "numero_telefone": numero_telefone,
                "cidade": cidade
            }

            if(self.cpf == usuario['cpf']):
                return print("Usuário já cadastrado!")

        self.cadastrado = True
        self.addClientes(userAdd)
        

    def addClientes(self, userAdd):       

        with open("clientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(userAdd)        
      

    def cadastrar(self):

        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        cpf = input("Digite seu cpf: ")
        celular = input("Digite seu celular: ")
        cidade = input("Digite sua cidade: ")

        self.nomeDono = nome
        self.idade = idade
        self.celular = celular
        self.cidade = cidade
        self.cpf = cpf

        userAdd = f"\n{nome},{cpf},{idade},{celular},{cidade}"
        self.verificacao(userAdd)

        

    