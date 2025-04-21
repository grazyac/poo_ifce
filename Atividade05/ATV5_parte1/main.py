from dia_dos_namorados import DiaDosNamorados
from natal import Natal
from aniversario import Aniversario

def main():
    destinatario = "Suziane"
    
    # Criando e exibindo os cartões
    cartoes = [
        DiaDosNamorados(destinatario),
        Natal(destinatario),
        Aniversario(destinatario)
    ]
    
    for cartao in cartoes:
        print(cartao.showMessage())
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()


    """O polimorfismo aqui permitiu escrever código genérico trabalhando com objetos diversos de 
    maneira uniforme, onde cada um manteve seu comportamento específico."""