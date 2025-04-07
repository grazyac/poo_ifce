from usuario import Usuario
import datetime 

class Conta:
    def __init__(self, agencia, usuario, data_abertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo
    
    def get_agencia(self):
        return self.agencia
    
    def get_usuario(self):
        return self.usuario
    
    def get_data_abertura(self):
        return self.data_abertura
    
    def get_saldo(self):
        return self.saldo