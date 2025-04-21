from cartao_web import CartaoWeb

class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)
    
    def showMessage(self) -> str:
        return (f"Meu amor {self.destinatario},\n\n"
                "Parabéns pelo seu dia!\n"
                "Desejo muita saúde, felicidade e sucesso em mais um ano da sua vida, que também é minha...\n"
                "Que todos os seus sonhos se realizem. Estarei sempre aqui.\n\n"
                "Com muito carinho, G. <3")