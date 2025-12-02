import json
import os

def carregar_alunos():
    arquivo_alunos = os.path.join("modulos", "alunos", "alunos.json")
    try:
        with open(arquivo_alunos, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def carregar_turmas():
    arquivo_turmas = os.path.join("modulos", "turmas", "turmas.json")
    try:
        with open(arquivo_turmas, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cabecalho(msg):
    tam = len(msg) + 4
    print("\n" + "=" * tam)
    print(f"  {msg}")
    print("=" * tam)

def relatorio_alunos_por_turma():
    cabecalho("RELATÓRIO: ALUNOS POR TURMA")
    
    alunos = carregar_alunos()
    turmas = carregar_turmas()
    
    if not turmas:
        print("\n Nenhuma turma cadastrada!")
        return
    
    if not alunos:
        print("\n Nenhum aluno cadastrado!")
        return
    
    alunos_por_turma = {}
    alunos_sem_turma = []
    total_idades = 0
    total_alunos = 0
    
    for aluno in alunos:
        total_alunos += 1
        total_idades += int(aluno.get("Idade", 0))
        
        cod_turma = aluno.get("cod_turma")
        if cod_turma:
            if cod_turma not in alunos_por_turma:
                alunos_por_turma[cod_turma] = []
            alunos_por_turma[cod_turma].append(aluno)
        else:
            alunos_sem_turma.append(aluno)
    
    for turma in turmas:
        cod = turma["cod_turma"]
        print(f"\n Turma {cod} - Período: {turma['periodo']} | Sala: {turma['sala']} | Turno: {turma['turno']}")
        print(f"   Capacidade: {turma['capacidade']}")
        
        if cod in alunos_por_turma:
            print(f"   Alunos matriculados: {len(alunos_por_turma[cod])}")
            for aluno in alunos_por_turma[cod]:
                print(f"   - Mat. {aluno['Matricula']}: {aluno['Nome']} ({aluno['Curso']})")
        else:
            print("Nenhum aluno matriculado nesta turma")
    
    if alunos_sem_turma:
        print(f"\n ALUNOS SEM TURMA DEFINIDA ({len(alunos_sem_turma)}):")
        for aluno in alunos_sem_turma:
            print(f"   - Mat. {aluno['Matricula']}: {aluno['Nome']} ({aluno['Curso']})")
    
    media_idade = total_idades / total_alunos if total_alunos > 0 else 0
    
    cabecalho("Relatório integrado - Resumo Geral")
    print(f"\n Total de alunos: {total_alunos}")
    print(f" Total de turmas: {len(turmas)}")
    print(f" Média de idade: {media_idade:.1f} anos")
    print(f" Alunos com turma: {total_alunos - len(alunos_sem_turma)}")
    print(f" Alunos sem turma: {len(alunos_sem_turma)}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    relatorio_alunos_por_turma()
    input("\nPressione ENTER para voltar...")
