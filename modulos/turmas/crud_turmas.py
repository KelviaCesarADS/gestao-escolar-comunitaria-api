import json
import os

ARQUIVO_PASTA = os.path.join(os.path.dirname(__file__), "turmas.json")

def carregar_turmas():
    if os.path.exists(ARQUIVO_PASTA):
        with open(ARQUIVO_PASTA, "r", encoding="utf-8") as t:
            return json.load(t)
    return[]

def salvar_turmas():
    if os.path.exists(ARQUIVO_PASTA):
        with open(ARQUIVO_PASTA, "w", encoding="utf-8") as t:
            return json.dump(t)
    return[]

def menu_turmas():
    print(f"--Menu administrativo Turmas--\n")
    opcao = input(int(print(f"\nVocê gostaria de: \n[1] Cadastrar nova turma\n[2] Atualizar uma turma\n[3]Deletar uma turma\n[4] Listar turmas")))
    while True:    
        match opcao:
            case 1:
                print("Você escolheu cadastrar uma nova turma.")
                cadastrar_turmas()
                continue
            case 2:
                print("Você escolheu atualizar uma turma.")
                atualizar_turma()
                continue
            case 3:
                print("Você escolheu deletar uma turma.")
                deletar_turma()
                continue
            case 4:
                print("Você escolheu listar as turmas")
                opcao = input(int("\nVocê gostaria de:\n[1] listar uma turma\n[2]Listar todas as turmas"))
                while True:
                    if opcao == 1:
                        Ler_tdsturmas()
                    elif opcao == 2:
                        ler_umaturma()
                    else:
                        opcao = input(int(print("Opção inválida, tente novamente.")))
                        continue
                continue       
            case 5:
                print("Você escolheu sair.")
                break
            case __:
                print("Opção inválida")
                continue

def deletar_turma(turmas):
    carregar_turmas(turmas)
    if not turmas:
        print(f"Não há turmas cadastradas ainda.\n")
        return
    try:
        id_turma = int(input("Iforme o ID da turma que será excluída: "))
        for t in turmas:
            if t["id"] == id_turma:
                confirmar = input(f"Tem certeza que deseja excluir a turma '{t['ano_serie']}' (ID {id_turma})? (s/n): ").strip().lower()
                if confirmar == 's':
                    turmas.remove(t)
                    salvar_turmas(turmas)
                    print(f"A turma '{t['ano_serie']}' removida com sucesso!\n")
                    return
                else:
                    print(f"Operação cancelada.\n")
        print(f"Essa turma não foi encontrada.\n")
    except ValueError:
        print(f"Este ID é inválido.\n")

def atualizar_turma(turmas):
    carregar_turmas(turmas)
    if not turmas:
        print(f"Não há turmas cadastradas ainda.\n")
        return
    try:
        id_turma = int(input("Informe o ID da turma que será atualizada: "))
        for t in turmas:
            if t["id"] == id_turma:
                print(f"Editando: {t["Ano ou Serie da turma: "]}")
                opcao = input(f"O que voçe gostaria de atualizar? [1] Ano ou serie\n [2] Sala\n [3] Turno\n [4] Capacidade\n [5] Sair\n")
                match opcao:
                    case 1:
                        t['ano_turma'] = input("Informe a informação atualizada: ")
                        salvar_turmas(turmas)
                        print(f"A turma foi atualizada com sucesso!\n")
                        continue
                    case 2:
                        t['sala'] = input("Informe a informação atualizada: ")
                        salvar_turmas(turmas)
                        print(f"A turma foi atualizada com sucesso!\n")
                        continue
                    case 3:
                        t['turno'] = input("Informe a informação atualizada: ")
                        salvar_turmas(turmas)
                        print(f"A turma foi atualizada com sucesso!\n")
                        continue
                    case 4:
                        t['capacidade'] = input("Informe a informação atualizada: ")
                        salvar_turmas(turmas)
                        print(f"A turma foi atualizada com sucesso!\n")
                        continue
                    case 5:
                        print("Operação finalizada.")
                        break
                    case __:
                        print("Opção inválida, tente novamente.")
                        continue
                return
        print(f"Essa turma não foi encontrada.\n")
    except ValueError:
        print(f"Este ID é inválido.\n")