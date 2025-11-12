import json
import os

ARQUIVO_PASTA = os.path.join(os.path.dirname(__file__),"turmas.json")

def carregar_dados():
    try:
        with open(ARQUIVO_PASTA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    
    
def salvar_dados(turmas):
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
    salvar_dados(turmas)
    print(f"Turma {turma['cod_turma']} cadastrada!")

turmas = carregar_dados()
cadastrar_turmas(turmas)