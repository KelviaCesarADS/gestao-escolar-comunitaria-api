import json
import os

ARQUIVO_PASTA = os.path.join(os.path.dirname(__file__),"turmas.json")

def carregar_turmas():
    try:
        with open(ARQUIVO_PASTA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    
    
def salvar_turmas(turmas):
    with open(ARQUIVO_PASTA, "w", encoding="utf-8") as t:
        json.dump(turmas, t, ensure_ascii=False, indent=4)


def cadastrar_turmas(turmas):
    print("\n---------CADASTRO DE TURMAS---------")
    ano_turma = input("Informe o ano/série da turma: ")
    sala = int(input("Informe a sala: "))
    turno = input("Informe o turno (Manhã/Tarde/Noite): ")
    capacidade = int(input("Informe a capacidade da turma: "))

    turma = {
        "cod_turma": len(turmas)+1, 
        "ano_turma": ano_turma,
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
        print(f"ID: {t['cod_turma']} - {t['ano_turma']} - {t['sala']} - {t['turno']} - {t['capacidade']}")

def ler_umaturma(turmas):
    if not turmas:
        print("Nenhuma turma cadastrada!")
        return
    
    try:
        cod_turma = int(input("Informe o código da turma: "))
        for t in turmas:
            if t['cod_turma'] == cod_turma:
                print(f"Ano/Série da turma: {t['ano_turma']} - Sala: {t['sala']} - Turno: {t['turno']} - Capacidade: {t['capacidade']}\n")
                return
            print("Turma não encontrada!\n")
    except ValueError:
        print("Código inválido!\n")
   
