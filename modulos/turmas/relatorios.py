from .modulos.turmas.crud_turmas import carregar_turmas

def menu_relatorioturma():
    while True:
        print("-- Relatório de Turmas --")
        print("[1] Relatório Turmas por ano")
        print("[2] Relatório Salas alocadas")
        print("[3] Relatório Capacidade total de turmas")
        print("[4] Sair")
        opcao = int(input("Digite sua escolha: "))
        match opcao:
            case 1:
                print("-- Relatório Turmas por ano --")
                relatorio_anoturma()
            case 2:
                print("-- Relatório Salas alocadas --")
            case 3:
                print("-- Relatório capacidade total --")
            case 4:
                print("Saindo...")
                break
            case __:
                print("Opção invalida! Tente novamente.")

def relatorio_anoturma():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    ano_turma = {}
    for t in turmas:
        ano_turma = t['ano_turma'].title()
        ano_turma[ano_turma] = ano_turma.get(ano_turma, 0) + 1
    print("Quantidade de turmas por ano:")
    for ano_turma, quantidade in ano_turma.items():
        print(f"{ano_turma} : {quantidade}")
        print()

def relatorio_salas():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    print(f"Total de salas alocadas: {len(turmas)}")

def relatorio_capacidade():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
    capacidade = sum(t{"capacidade"} for t in turmas)
    print(f"A quantidade de alunos registrados em turmas é: {capacidade}")


