from metodo_pgto import MetodoPagamento

class Boleto(MetodoPagamento):
    def pagar(self) -> None:
        desconto = 0.02
        valor_final = self.valor * (1 - desconto)
        
        print("\n Pagamento com Boleto Bancário")
        print(f"• Valor original: R$ {self.valor:.2f}")
        print(f"• Desconto (2%): R$ {self.valor * desconto:.2f}")
        print(f"• Valor final: R$ {valor_final:.2f}")
        print("Boleto gerado com sucesso!")