# adicionar um produto ao estoque
def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso!")

# remover um produto do estoque
def remover_produto(estoque):
    nome = input("Digite o nome do produto a ser removido: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

# atualizar a quantidade de um produto
def atualizar_quantidade(estoque):
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        estoque[nome] = nova_quantidade
        print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

# exibir todos os produtos no estoque
def exibir_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

# função principal
def gerenciar_estoque():
    estoque = {}
    while True:
        print("\n--- Menu de Gerenciamento de Estoque ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar quantidade")
        print("4. Exibir estoque")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            remover_produto(estoque)
        elif opcao == "3":
            atualizar_quantidade(estoque)
        elif opcao == "4":
            exibir_estoque(estoque)
        elif opcao == "5":
            print("Saindo do sistema de estoque...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# executar
gerenciar_estoque()