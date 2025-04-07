class Livro:
    
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco    

    def mostrar_infos(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Preço: R${self.preco:.2f}")

# Criando dois livros
livro1 = Livro("Morro dos Ventos Uivantes", "Emily Brontë", 1847, 34.90)
livro2 = Livro("De quanta terra precisa um homem? e outras histórias", "Liev Tolstói", 1886, 29.90)

livro1.mostrar_infos()
livro2.mostrar_infos()