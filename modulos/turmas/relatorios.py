from .modulos.turmas.crud_turmas import carregar_turmas

def menu_relatorioturma():
    while True:
        print("-- Relatório de Turmas --")
        print("[1] Relatório Turmas por ano")
        print("[2] Relatório Salas alocadas")
        print("[3] Relatório Capacidade total de turmas")
        print("[4] Relatório Turnos")
        print("[5] Sair")
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
                print("-- Relátorio Turnos --")
            case 5:
                print("Saindo...")
                break
            case __:
                print("Opção invalida! Tente novamente.")

def relatorio_periodoturma():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    periodo = {}
    for t in turmas:
        periodo = t['periodo'].title()
        periodo[periodo] = periodo.get(periodo, 0) + 1
    print("Quantidade de turmas por ano:")
    for periodo, quantidade in periodo.items():
        print(f"{periodo} : {quantidade}")
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
    soma = sum(t["capacidade"] for t in turmas)
    print(f"A quantidade de alunos registrados em turmas é: {soma}")

def relatorio_turnos():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")


