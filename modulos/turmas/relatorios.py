import json
import os

ARQUIVO_PASTA = os.path.join(os.path.dirname(__file__), "turmas.json")

def carregar_turmas():
    try:
        with open(ARQUIVO_PASTA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]


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
                relatorio_periodoturma()
            case 2:
                print("-- Relatório Salas alocadas --")
                relatorio_salas()
            case 3:
                print("-- Relatório capacidade total --")
                relatorio_capacidade()
            case 4:
                print("-- Relátorio Turnos --")
                relatorio_turnos()
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
    periodos = {}
    for t in turmas:
        periodo = t.get('periodo').title()
        periodos[periodo] = periodos.get(periodo, 0) + 1

    print("-- Quantidade de turmas por período/ano --")
    for periodo, quantidade in periodos.items():
        print(f"{periodo}: {quantidade}")
    print()

def relatorio_salas():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    print(f"-- Total de salas alocadas: {len(turmas)} --")

def relatorio_capacidade():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas.")
        return
    soma = sum(t["capacidade"] for t in turmas)
    print(f"-- A capacidade total de alunos em turmas alocadas é: {soma} --")

def relatorio_turnos():
    turmas = carregar_turmas()

    if not turmas:
        print("Não há turmas cadastradas.")
        return

    turnos = {}

    for turma in turmas:
        turno = turma.get("turno", "Não informado").title()
        turnos[turno] = turnos.get(turno, 0) + 1

    print("-- Quantidade de turmas por turno --")
    for turno, quantidade in turnos.items():
        print(f"{turno}: {quantidade}")
    print()
