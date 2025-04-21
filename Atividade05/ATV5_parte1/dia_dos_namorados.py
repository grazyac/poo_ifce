from cartao_web import CartaoWeb

class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)
    
    def showMessage(self) -> str:
        return (f"Querida {self.destinatario},\n\n"
                "Neste Dia dos Namorados, gostaria de dizer que a amo muito e que me faz muito feliz!\n"
                "Que possamos compartilhar muitos momentos felizes juntas.\n\n"
                "Com todo meu amor,\n"
                "Sua eterna namorada, G. <3")