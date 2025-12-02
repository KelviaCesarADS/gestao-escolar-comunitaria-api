import json
import os
from relatorios import menu_relatorioturma

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
    while True:
        print("Você gostaria de: ")
        print("[1] Cadastrar nova turma")
        print("[2] Atualizar uma turma")
        print("[3] Deletar uma turma")
        print("[4] Listar turmas")
        print("[5] Relátorios das turmas")
        print("[6] Sair")
        opcao = int(input("Informe sua escolha: "))
        match opcao:
            case 1:
                print("Você escolheu cadastrar uma nova turma.")
                turmas = carregar_turmas()
                cadastrar_turmas(turmas)
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
                turmas = carregar_turmas()
                opcao_lista = int(input("Digite sua escolha: "))
                if opcao_lista == 1:
                    ler_umaturma(turmas)
                elif opcao_lista == 2:
                    ler_tdsturmas(turmas)
                else:
                    print("Opção inválida, tente novamente.")
            case 5:
                print("Acessando menu de relátorios da turma.")
                menu_relatorioturma()
            case 6:
                print("Saindo...")
                break
            case __:
                print("Opção inválida")

def cadastrar_turmas(turmas):
    print("\n---------CADASTRO DE TURMAS---------")
    while True:
        periodo = input("Informe o período da turma: (Ex: 2025.1)").strip()
        if periodo != "":
            break
        print("O período não pode ficar vazio. Utilize o exemplo informado.")
    while True:        
        sala = int(input("Informe a sala: "))
        if sala > 0:
            break
        else:
            print("O número da sala deve ser maior que 0. Ex: Sala 101, 201, 301.")
    turnos = ["MANHÃ", "TARDE", "NOITE"]
    while True:
        turno = input("Informe o turno (MANHÃ/TARDE/NOITE): ")
        if turno in turnos:
            break
        else:
            print("Turno inválido. Utilize o exemplo informado!")
    while True:            
        capacidade = int(input("Informe a capacidade da turma: "))
        if capacidade > 0:
            break
        else:
            print("A capacidade da turma deve ser superior a 0. Informe novamente!")

    turma = {
        "cod_turma": len(turmas)+1, 
        "periodo": periodo,
        "sala": sala,
        "turno": turno,
        "capacidade": capacidade
    }

    turmas.append(turma)
    salvar_turmas(turmas)
    print(f"Turma {turma['cod_turma']} cadastrada!")


def ler_tdsturmas(turmas):
    if not turmas:
        print("Nenhuma turma cadastrada!")
        return
    
    print("Listando turmas...: ")
    for t in turmas:
        print(f"ID: {t['cod_turma']} - {t['periodo']} - {t['sala']} - {t['turno']} - {t['capacidade']}")

def ler_umaturma(turmas):
    if not turmas:
        print("Nenhuma turma cadastrada!")
        return
    
    try:
        cod_turma = int(input("Informe o código da turma: "))
        for t in turmas:
            if t['cod_turma'] == cod_turma:
                print(f" Período da turma: {t['periodo']} - Sala: {t['sala']} - Turno: {t['turno']} - Capacidade: {t['capacidade']}\n")
                return
            print("Turma não encontrada!\n")
    except ValueError:
        print("Código inválido!\n")
       
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
                print(f"Editando turma de período {t['periodo']} e sala {t['sala']}")
                while True:
                    print("O que você gostaria de atualizar?")
                    print("[1] Período")
                    print("[2] Sala")
                    print("[3] Turno")
                    print("[4] Capacidade")
                    print("[5] Finalizar e salvar")

                    opcao = int(input("Digite sua escolha: "))
                    match opcao:
                        case 1:
                            while True:
                                t['periodo'] = input("Nova informação: (Ex:2025.1)")
                                if t['periodo'] != "":
                                    break
                                else:
                                    print("Informe o período novamente no formato indicado! (Ex:2026.6)")
                        case 2:
                            while True:
                                t['sala'] = int(input("Nova informação: "))
                                if t['sala'] > 0:
                                    break
                                else:
                                    print("A sala deve ser um número positivo! Ex: 101, 204, 405")
                        case 3:
                            turnos = ["MANHÃ", "TARDE", "NOITE"]
                            while True:
                                t['turno'] = input("Nova informação (MANHÃ/TARDE/NOITE): ")
                                if (t['turno']) in turnos:
                                    break
                                else:
                                    print("Turnos devem ser MANHÂ, TARDE OU NOITE. Informe novamente!")
                        case 4:
                            while True:
                                t['capacidade'] = int(input("Nova informação: "))
                                if t['capacidade'] > 0:
                                    break
                                else:
                                    print("A capacidade deve ser acima de 0")
                        case 5:
                            print("Operação finalizada.")
                            break
                        case _:
                            print("Opção inválida.")

                    salvar_turmas(turmas)
                    print("Turma atualizada com sucesso!")
                    return
        print("Essa turma não foi encontrada.")
    except ValueError:
        print("Este ID é inválido.")

if __name__ == "__main__":
    menu_turmas()
    