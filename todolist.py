tarefas = []

def mostrar_menu():
    print("\n📝 MENU - Lista de Tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("✅ Tarefa adicionada!")

    elif escolha == "2":
        if tarefas:
            print("\n📋 Tarefas:")
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t}")
        else:
            print("📭 Nenhuma tarefa ainda!")

    elif escolha == "3":
        if tarefas:
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t}")
            indice = int(input("Digite o número da tarefa para remover: ")) - 1
            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print(f"❌ Tarefa '{removida}' removida.")
            else:
                print("Número inválido.")
        else:
            print("📭 Nenhuma tarefa para remover.")

    elif escolha == "4":
        print("👋 Saindo... Até logo!")
        break

    else:
        print("⚠️ Opção inválida! Tente novamente.")
