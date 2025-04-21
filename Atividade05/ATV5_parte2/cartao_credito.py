from metodo_pgto import MetodoPagamento

class CartaoCredito(MetodoPagamento):
    def pagar(self) -> None:
        taxa = 0.05
        valor_final = self.valor * (1 + taxa)
        
        print("\n Pagamento com Cartão de Crédito")
        print(f"• Valor original: R$ {self.valor:.2f}")
        print(f"• Taxa (5%): R$ {self.valor * taxa:.2f}")
        print(f"• Valor final: R$ {valor_final:.2f}")
        print("Transação aprovada!")