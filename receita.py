class receita:

    def __init__(self):
        self.receita = [] * 2
    
    def gastos(self, valor): 
        with open("./receita/receita.csv", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 
            valores = i.replace("\n", "") 
            
            ganhos, gastos, lucro = i.split(",")

        atualizacao = f"{ganhos},{int(gastos) + valor},{int(ganhos) - (int(gastos) + valor)}"
        
        with open("./receita/receita.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{atualizacao}\n")

    
    def ganhos(self, valor):
        with open("./receita/receita.csv", "r", encoding="utf-8") as arquivo:
            c = arquivo.readlines()
        
        for i in c: 
            valores = i.replace("\n", "") 
            self.receita.append(valores)  
            
            ganhos, gastos, lucro = i.split(",")
        
        lucro = (int(ganhos) + valor) - int(gastos)
        atualizacao = f"{int(ganhos)+valor},{gastos},{lucro}"
        
        with open("./receita/receita.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{atualizacao}\n")