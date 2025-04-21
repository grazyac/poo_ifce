from metodo_pgto import MetodoPagamento

class Pix(MetodoPagamento):
    def pagar(self) -> None:
        print("\n Pagamento via Pix")
        print(f"• Valor: R$ {self.valor:.2f}")
        print("• Sem taxas ou descontos")
        print("Pagamento realizado instantaneamente!")