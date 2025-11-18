
import json
import os

armazenamento_dados = "alunos.json"

def leitura_dados():
    if not os.path.exists(armazenamento_dados):
        return {}
    with open(armazenamento_dados, "r", encoding="utf-8") as f:
        return json.load(f)

def listar_alunos(dados):
    if not dados:
        print("Nenhum aluno cadastrado.")
        return
    print("--- LISTA DE ALUNOS ---")
    for matricula, aluno in dados.items():
        print(f"{matricula} | {aluno['nome']} | {aluno['idade']} anos | Turma: {aluno['turma']}")
    print("------------------------")

def buscar_alunos(dados):
    if not dados:
        print("Nenhum aluno cadastrado.")
        return
    buscar = input("Digite a matrícula ou nome para buscar: ").lower().strip()
    resultados = []
    for matricula, aluno in dados.items():
        if buscar in matricula.lower() or buscar in aluno["nome"].lower():
            resultados.append((matricula, aluno))
    if resultados:
        print(f"{len(resultados)} resultado(s) encontrado(s):")
        for matricula, aluno in resultados:
            print(f"{matricula} | {aluno['nome']} | {aluno['idade']} anos | Turma: {aluno['turma']}")
    else:
        print("Nenhum aluno encontrado.")

def relatorio(dados):
    if not dados:
        print("Nenhum aluno cadastrado.")
        return
    total_alunos = len(dados)
    idade_alunos = [aluno["idade"] for aluno in dados.values()]
    media_idade_alunos = sum(idade_alunos) / total_alunos if total_alunos > 0 else 0
    turmas = {}
    for aluno in dados.values():
        turma = aluno["turma"]
       
        turmas[turma] = turmas.get(turma, 0) + 1
    print("\n=== RELATÓRIO GERAL DE ALUNOS ===")
    print(f" Total de alunos: {total_alunos}")
    print(f" Média de idade: {media_idade_alunos:.1f} anos")
    print(" Alunos por turma:")
    for turma, qtd in turmas.items():
        print(f"  - {turma}: {qtd} aluno(s)")
    print("----------------------------------")

def menu():
    
    dados = leitura_dados()
    while True:
        print("\n---- SISTEMA DE CONSULTA DE ALUNOS ----")
        print("1. Listar alunos")
        print("2. Buscar aluno")
        print("3. Gerar relatório")
        print("0. Sair")
        print("---------------------------------------")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            listar_alunos(dados)
        elif opcao == "2":
            buscar_alunos(dados)
        elif opcao == "3":
            relatorio(dados)
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

