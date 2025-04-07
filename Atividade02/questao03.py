class Carro:
   
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca  
        self.modelo = modelo  
        self.ano = ano  
        self.cor = cor  

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}), Cor: {self.cor}"

# Criando dois carros
meu_carro = Carro("Fiat", "Cronos", 2022, "Azul")
carro_irmao = Carro("Nissan", "Sentra", 2018, "Crinza")

print("Meu carro:", meu_carro)
print("Carro do meu irmão:", carro_irmao) 