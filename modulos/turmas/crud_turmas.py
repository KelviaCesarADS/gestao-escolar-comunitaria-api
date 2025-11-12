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
            return json.load(t)
    return[]


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