from cartao_web import CartaoWeb

class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)
    
    def showMessage(self) -> str:
        return (f"Querida {self.destinatario},\n\n"
                "Que esta época natalina traga muita paz, alegria e harmonia.\n"
                "Que 2025 seja repleto de conquistas!\n\n"
                "Feliz Natal e Próspero Ano Novo!\n"
                "Com carinho, G. <3")