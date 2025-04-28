
from veiculos import Veiculo

def mostrar_titulo():
    print("SISTEMA DE LOCADORA DE VEÍCULOS")
    
def main():
    mostrar_titulo()
    
    print("Cadastrando veículos:")
    carro1 = Veiculo("ABC1D23", "Fiat Uno", 120.50)
    carro2 = Veiculo("XYZ9E87", "Volkswagen Fusca", 180.75)
    
    print("\nSituação inicial:")
    carro1.status()
    carro2.status()
    
    print("\nTestando aluguel:")
    carro1.alugar()
    carro1.status()
    
    print("\nTentando alugar novamente:")
    carro1.alugar()  
    
    print("\nDevolvendo veículo:")
    carro1.devolver()
    carro1.status()
    
    print("\nTestando alteração de placa:")
    print(f"Placa atual: {carro2.placa}")
    print("Tentando alterar...")
    carro2.placa = "NOVA123"  
    
    Veiculo.mostrar_total_veiculos()
    
    print("\nSimulando aluguel:")
    dias = 3
    total = Veiculo.calcular_preco_aluguel(dias, carro2.diaria)
    print(f"Aluguel do {carro2.modelo} por {dias} dias: R$ {total:.2f}")
    
    print("FIM DO PROGRAMA")
    
if __name__ == "__main__":
    main()