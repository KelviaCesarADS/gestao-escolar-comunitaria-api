import json
import os

ARQUIVO_PASTA = os.path.join(os.path.dirname(__file__), "turmas.json")

def carregar_turmas():
    try:
        with open(ARQUIVO_PASTA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]

def salvar_turmas(turmas):
    with open(ARQUIVO_PASTA, "w", encoding="utf-8") as t:
        return json.dump(turmas, t, ensure_ascii=False, indent=4)

def menu_turmas():
    print("--Menu administrativo Turmas--")
    print("Você gostaria de: ")
    print("[1] Cadastrar nova turma")
    print("[2] Atualizar uma turma")
    print("[3]Deletar uma turma")
    print("[4] Listar turmas")
    print("[5] Sair")
    while True:
        opcao = int(input("Informe sua escolha: "))
        match opcao:
            case 1:
                print("Você escolheu cadastrar uma nova turma.")
                cadastrar_turmas()
            case 2:
                print("Você escolheu atualizar uma turma.")
                atualizar_turma()
            case 3:
                print("Você escolheu deletar uma turma.")
                deletar_turma()
            case 4:
                print("Você escolheu listar as turmas")
                print("Você gostaria de:")
                print("[1] listar uma turma")
                print("[2]Listar todas as turmas")
                while True:
                    opcao = int(input("Digite sua escolha: "))
                    if opcao == 1:
                        Ler_tdsturmas()
                    elif opcao == 2:
                        ler_umaturma()
                    else:
                        opcao = input(int(print("Opção inválida, tente novamente.")))
            case 5:
                print("Saindo...")
                break
            case __:
                print("Opção inválida")
    

def deletar_turma():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas ainda.")
        return
    try:
        cod_turma = int(input("Iforme o ID da turma que será excluída: "))
        for t in turmas:
            if t["cod_turma"] == cod_turma:
                confirmar = input(f"Tem certeza que deseja excluir a turma '{t['sala']}' (ID {cod_turma})? (s/n): ").strip().lower()
                if confirmar == 's':
                    turmas.remove(t)
                    salvar_turmas(turmas)
                    print(f"A turma '{t['sala']}' removida com sucesso!\n")
                    return
                else:
                    print("Operação cancelada.")
                    return
        print("Essa turma não foi encontrada.")
    except ValueError:
        print("Este ID é inválido.")

def atualizar_turma():
    turmas = carregar_turmas()
    if not turmas:
        print("Não há turmas cadastradas ainda.")
        return
    try:
        cod_turma = int(input("Informe o ID da turma que será atualizada: "))
        for t in turmas:
            if t["cod_turma"] == cod_turma:
                print(f"Editando: {t['ano_turma']}")
                print("O que você gostaria de atualizar?")
                print("[1] Ano ou série")
                print("[2] Sala")
                print("[3] Turno")
                print("[4] Capacidade")
                print("[5] Sair")

                opcao = int(input("Digite sua escolha: "))
                match opcao:
                    case 1:
                        t['ano_turma'] = input("Nova informação: ")
                    case 2:
                        t['sala'] = input("Nova informação: ")
                    case 3:
                        t['turno'] = input("Nova informação: ")
                    case 4:
                        t['capacidade'] = input("Nova informação: ")
                    case 5:
                        print("Operação finalizada.")
                        return
                    case _:
                        print("Opção inválida.")
                        return

                salvar_turmas(turmas)
                print("Turma atualizada com sucesso!")
                return
        print("Essa turma não foi encontrada.")
    except ValueError:
        print("Este ID é inválido.")

menu_turmas()