from restaurante import Restaurante

def criar_restaurantes():
    return [
        Restaurante("Sabor da Casa", "comida brasileira"),
        Restaurante("Paste e Specialitá", "comida italiana"),
        Restaurante("Takun Tudo", "comida japonesa")
    ]

def mostrar_descricoes(restaurantes):
    print("\nUsando o método descrever_restaurante:")
    for restaurante in restaurantes:
        restaurante.descrever_restaurante()
    
    print("\nAgora usando o __str__:")
    for restaurante in restaurantes:
        print(restaurante)

def testar_abertura(restaurantes):
    print("\nAbrindo os restaurantes:")
    for restaurante in restaurantes:
        restaurante.abrir_restaurante()

def main():
    restaurantes = criar_restaurantes()
    mostrar_descricoes(restaurantes)
    testar_abertura(restaurantes)

if __name__ == "__main__":
    main()