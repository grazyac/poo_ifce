class Pessoa:
    
    def __init__(self, nome, idade, cidade):
        self.nome = nome    
        self.idade = idade  
        self.cidade = cidade  

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}.")

# Criando duas pessoas
amigo1 = Pessoa("Grazi", 36, "Fortaleza")
amigo2 = Pessoa("Suzi", 39, "Maranguape")

# Chamando o método apresentar() para cada um
amigo1.apresentar()  
amigo2.apresentar()