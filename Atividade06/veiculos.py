
class Veiculo:
     
    total_veiculos = 0  
    
    def __init__(self, placa, modelo, diaria):
        self.__placa = placa
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False
        Veiculo.total_veiculos += 1
        
        print(f"Veículo {modelo} cadastrado. Placa: {placa}")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        print("A placa não pode ser alterada após o cadastro.")

    def alugar(self):
        if self.__alugado:
            print(f"{self.modelo} já está alugado.")
        else:
            self.__alugado = True
            print(f"{self.modelo} alugado com sucesso.")

    def devolver(self):
        if not self.__alugado:
            print(f"{self.modelo} já está disponível.")
        else:
            self.__alugado = False
            print(f"{self.modelo} devolvido.")

    def status(self):
        situacao = "ALUGADO" if self.__alugado else "DISPONÍVEL"
        print(f"{self.modelo} [{self.placa}]: {situacao} (R$ {self.diaria:.2f}/dia)")

    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"\nTotal de veículos na locadora: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        if dias < 1:
            return 0.0
        return dias * diaria