# adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"Título": titulo, "Descrição": descricao, "Status": "Pendente"}
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

# marcar uma tarefa como concluída
def marcar_concluida(tarefas):
    titulo = input("Digite o título da tarefa concluída: ")
    for tarefa in tarefas:
        if tarefa["Título"] == titulo:
            tarefa["Status"] = "Concluído"
            print(f"Tarefa '{titulo}' marcada como concluída!")
            return
    print(f"Tarefa '{titulo}' não encontrada.")

# listar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Tarefas Pendentes ---")
        for tarefa in tarefas:
            if tarefa["Status"] == "Pendente":
                print(f"Título: {tarefa['Título']}, Descrição: {tarefa['Descrição']}")
        
        print("\n--- Tarefas Concluídas ---")
        for tarefa in tarefas:
            if tarefa["Status"] == "Concluído":
                print(f"Título: {tarefa['Título']}, Descrição: {tarefa['Descrição']}")

# função principal
def gerenciar_tarefas():
    tarefas = []
    while True:
        print("\n--- Menu de Gerenciamento de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Listar tarefas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            marcar_concluida(tarefas)
        elif opcao == "3":
            listar_tarefas(tarefas)
        elif opcao == "4":
            print("Saindo do sistema de tarefas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# executar 
gerenciar_tarefas()