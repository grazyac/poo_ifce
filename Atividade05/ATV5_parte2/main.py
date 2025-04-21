from cartao_credito import CartaoCredito
from pix import Pix
from boleto import Boleto

def obter_valor() -> float:
    while True:
        try:
            valor = float(input("Valor da compra: R$ "))
            if valor <= 0:
                print("O valor deve ser positivo")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico válido")

def selecionar_metodo(valor: float):
    while True:
        print("\n Métodos de Pagamento:")
        print("1. Cartão de Crédito (+5%)")
        print("2. Pix (sem taxas)")
        print("3. Boleto (-2%)")
        
        opcao = input("Escolha (1-3): ")
        
        if opcao == "1":
            return CartaoCredito(valor)
        elif opcao == "2":
            return Pix(valor)
        elif opcao == "3":
            return Boleto(valor)
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("\n SISTEMA DE PAGAMENTO")
    
    valor = obter_valor()
    pagamento = selecionar_metodo(valor)
    pagamento.pagar()

if __name__ == "__main__":
    main()


    """Como o uso de polimorfismo facilitou a implementação do sistema de pagamento? 
    Quais seriam as vantagens de usar uma interface abstrata nesse contexto realista?
    
    O polimorfismo simplificou o sistema quando uma unica chamada se adaptou a cada método
    bastanto criar classes e mantendo a lógica. As vantagens: simplificou, padronizou e 
    a mudança nas regras dos métodos não altera os demais."""