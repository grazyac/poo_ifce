# adicionar um aluno e suas notas
def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} (N{i+1}): "))
        notas.append(nota)
    alunos[nome] = notas
    print(f"Aluno '{nome}' cadastrado com sucesso!")

# atualizar as notas de um aluno
def atualizar_notas(alunos):
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        notas = []
        for i in range(4):
            nota = float(input(f"Digite a nova nota {i+1} (N{i+1}): "))
            notas.append(nota)
        alunos[nome] = notas
        print(f"Notas do aluno '{nome}' atualizadas com sucesso!")
    else:
        print(f"Aluno '{nome}' não encontrado.")

# remover um aluno
def remover_aluno(alunos):
    nome = input("Digite o nome do aluno a ser removido: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno '{nome}' removido com sucesso!")
    else:
        print(f"Aluno '{nome}' não encontrado.")

# calcular e exibir a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# exibir todos os alunos e suas médias
def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos e suas médias:")
        for nome, notas in alunos.items():
            media = calcular_media(notas)
            print(f"{nome}: Notas = {notas}, Média = {media:.2f}")

# função principal
def gerenciar_alunos():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }
    while True:
        print("\n--- Menu de Gerenciamento de Alunos ---")
        print("1. Adicionar aluno")
        print("2. Atualizar notas")
        print("3. Remover aluno")
        print("4. Exibir alunos e médias")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            atualizar_notas(alunos)
        elif opcao == "3":
            remover_aluno(alunos)
        elif opcao == "4":
            exibir_alunos(alunos)
        elif opcao == "5":
            print("Saindo do sistema de alunos...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# executar 
gerenciar_alunos()