class Restaurante:
       
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome = nome_restaurante
        self.cozinha = tipo_cozinha
    
    def descrever_restaurante(self):
        print(f"O restaurante {self.nome} serve especialidades da culinária {self.cozinha}.")
    
    def abrir_restaurante(self):
        print(f"{self.nome} está pronto para servir você.")
    
    def __str__(self):
        return f"Restaurante: {self.nome} | Especialidade: {self.cozinha}"