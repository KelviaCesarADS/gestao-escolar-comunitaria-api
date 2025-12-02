lista_de_alunos = []
num_matricula = 1
import json
import os
NOME_ARQUIVO = os.path.join(os.path.dirname(__file__), "alunos.json")

def carregar_dados():
    """Carrega a lista de alunos do arquivo JSON ao iniciar o programa."""
    global lista_de_alunos, num_matricula
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
            lista_de_alunos = json.load(f)
            
            if lista_de_alunos:
                num_matricula = max(aluno['Matricula'] for aluno in lista_de_alunos) + 1
            else:
                num_matricula = 1
                
    except FileNotFoundError:
        lista_de_alunos = []
        num_matricula = 1
        
    except json.JSONDecodeError:
        print(f"Aviso: Arquivo '{NOME_ARQUIVO}' inválido. Iniciando com lista vazia.")
        lista_de_alunos = []
        num_matricula = 1

def salvar_dados():
    """Salva a lista de alunos atual no arquivo JSON."""
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(lista_de_alunos, f, indent=4)
        print(f"Dados salvos com sucesso em '{NOME_ARQUIVO}'.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def cabecalho(msg):
    tam = len(msg) + 4
    print("-"*tam)
    print(f"  {msg}")
    print("-"*tam)

def adicionar_alunos():
    global num_matricula
    cabecalho("Matriculando Aluno")

    nome_aluno = input("\nDigite o nome do aluno: ")
    idade_aluno = input("\nDigite a idade do aluno: ")
    genero_aluno = input("\nDigite o gênero do aluno: ")
    curso_aluno = input("\nQual o curso que o aluno está fazendo: ")
    periodo_aluno = input("\nQual o período que o aluno está: ")
    turma_aluno = input("\nCódigo da turma (deixe em branco se não souber): ").strip()

    aluno = {
        "Matricula": num_matricula,
        "Nome": nome_aluno,
        "Idade": idade_aluno,
        "Genero": genero_aluno,
        "Curso": curso_aluno,
        "Periodo": periodo_aluno
    }
    
    if turma_aluno:
        try:
            aluno["cod_turma"] = int(turma_aluno)
        except ValueError:
            pass

    lista_de_alunos.append(aluno)
    num_matricula += 1
    print(f"\nO aluno {nome_aluno} foi matriculado com sucesso!")
    salvar_dados()

def ver_dados_alunos():
    cabecalho("Lista de Alunos Matriculados")

    if not lista_de_alunos:
        print("Nenhum aluno matriculado!")
        return

    for aluno in lista_de_alunos:
        print(f"Matricula: {aluno["Matricula"]} | Nome: {aluno["Nome"]} | Curso: {aluno["Curso"]} | Periodo: {aluno["Periodo"]}")

def atualizar_lista_alunos():
    ver_dados_alunos()

    try:
        matricula_procurada = int(input("Digite o número de matricula do aluno que deseja atualizar o cadastro: "))
    except ValueError:
        print("Entrada inválida!")
        return

    aluno_encontrado = None
    
    for aluno in lista_de_alunos:
        if aluno["Matricula"] == matricula_procurada:
            aluno_encontrado = aluno
            break
    
    if aluno_encontrado:
        print(f"\nAluno encontrado: {aluno_encontrado['Nome']} Mátricula: {aluno_encontrado['Matricula']}")
        print(" --- Insira os novos dados (Deixar em branco os que não quiser alterar! --- )")

        novo_nome = input(f"Novo nome: ({aluno_encontrado['Nome']}): ")
        nova_idade = input(f"Nova Idade ({aluno_encontrado['Idade']}): ")
        novo_genero = input(f"Novo Gênero: ({aluno_encontrado['Genero']}): ")
        novo_curso = input(f"Novo Curso: ({aluno_encontrado['Curso']}): ")
        novo_periodo = input(f"Novo Periodo ({aluno_encontrado['Periodo']}): ")
        nova_turma = input(f"Código da turma (atual: {aluno_encontrado.get('cod_turma', 'Nenhuma')}): ").strip()

        if novo_nome:
            aluno_encontrado["Nome"] = novo_nome
            
        if nova_idade:
            aluno_encontrado["Idade"] = nova_idade
            
        if novo_genero:
            aluno_encontrado["Genero"] = novo_genero
        
        if novo_curso:
            aluno_encontrado["Curso"] = novo_curso
        
        if novo_periodo:
            aluno_encontrado["Periodo"] = novo_periodo
        
        if nova_turma:
            try:
                aluno_encontrado["cod_turma"] = int(nova_turma)
            except ValueError:
                pass
            
        print(f"\n Dados da matrícula {matricula_procurada} atualizados com sucesso!")
        salvar_dados()
        
    else:
        print(f"\n Matrícula {matricula_procurada} não encontrada.")

def buscar_alunos(lista_de_alunos):
    cabecalho("Buscar Alunos")
    
    if not lista_de_alunos:
        print("Nenhum aluno cadastrado.")
        return
        
    buscar = input("Digite a matrícula ou nome para buscar: ").lower().strip()
    resultados = []
    
    for aluno in lista_de_alunos: 
        matricula_str = str(aluno["Matricula"])
        
        if buscar in matricula_str or buscar in aluno["Nome"].lower():
            resultados.append(aluno)
            
    if resultados:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):")
        
        for aluno in resultados:
            print(f"Matrícula: {aluno['Matricula']} | Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | Curso: {aluno['Curso']}")
            
    else:
        print("Nenhum aluno encontrado.")

def gerar_relatorio(lista_de_alunos):
    cabecalho("RELATÓRIO GERAL DE ALUNOS")
    
    if not lista_de_alunos:
        print("Nenhum aluno cadastrado.")
        return
        
    total_alunos = len(lista_de_alunos)
    
    idade_alunos = [int(aluno["Idade"]) for aluno in lista_de_alunos] 
    
    media_idade_alunos = sum(idade_alunos) / total_alunos if total_alunos > 0 else 0
    
    contagem_cursos = {} 
    
    for aluno in lista_de_alunos: 
        curso = aluno["Curso"] 
        
        contagem_cursos[curso] = contagem_cursos.get(curso, 0) + 1
        
    print(f" Total de alunos: {total_alunos}")
    print(f" Média de idade: {media_idade_alunos:.1f} anos")
    
    print("\n Alunos por Curso:")
    for curso, qtd in contagem_cursos.items(): 
        print(f"  - {curso}: {qtd} aluno(s)")
    print("-" * 30)

def excluir_matricula():
    ver_dados_alunos()
    matricula_procurada = int(input("Digite o número de matricula que queira excluir: "))
    
    aluno_removido = None
    indice_a_deletar = -1

    for i, aluno in enumerate(lista_de_alunos):
        if aluno['Matricula'] == matricula_procurada:
            indice_a_deletar = i
            break
            
    if indice_a_deletar != -1:
        aluno_removido = lista_de_alunos.pop(indice_a_deletar)
        
        print(f"✅ O aluno {aluno_removido['Nome']} foi excluído da lista!")
        salvar_dados()
        
    else:
        print(f"❌ Matrícula {matricula_procurada} não encontrada.")

carregar_dados()
while True:
    cabecalho("Menu Principal")
    print("\n --- Selecione a opção desejada ---")
    print("1 - Matricular aluno")
    print("2 - Ler lista de matriculados")
    print("3 - Atualizar matricula")
    print("4 - Buscar aluno")
    print("5 - Gerar relatório")
    print("6 - Excluir matrícula")
    print("7 - Sair")

    opcao = input("\nSelecione a opção desejada: ")

    if opcao == "1":
        adicionar_alunos()
    
    elif opcao == "2":
        ver_dados_alunos()
    
    elif opcao == "3":
        atualizar_lista_alunos()

    elif opcao == "4":
        buscar_alunos(lista_de_alunos)

    elif opcao == "5":
        gerar_relatorio(lista_de_alunos)

    elif opcao == "6":
        excluir_matricula()
        
    elif opcao == "7":
        salvar_dados()
        print("Operação Finalizada!")
        break

    else:
        print("Valor inválido! Selecione outra opção: ")