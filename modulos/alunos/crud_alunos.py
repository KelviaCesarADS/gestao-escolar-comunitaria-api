lista_de_alunos = []
num_matricula = 1

# Fazer um cabeçalho organizado
def cabecalho(msg):
    tam = len(msg) + 4
    print("-"*tam)
    print(f"  {msg}")
    print("-"*tam)

# Criando a lista de alunos matriculados
def adicionar_alunos():
    global num_matricula
    cabecalho("Matriculando Aluno")

    nome_aluno = input("\nDigite o nome do aluno: ")
    idade_aluno = input("\nDigite a idade do aluno: ")
    genero_aluno = input("\nDigite o gênero do aluno: ")
    curso_aluno = input("\nQual o curso que o aluno está fazendo: ")
    periodo_aluno = input("\nQual o período que o aluno está: ")

    aluno = {"Matricula": num_matricula, "Nome": nome_aluno, "Idade": idade_aluno, "Genero": genero_aluno, "Curso": curso_aluno, "Periodo": periodo_aluno}
    lista_de_alunos.append(aluno)
    num_matricula += 1
    print(f"\nO aluno {nome_aluno} foi matriculado com sucesso!")

# Visualizar a lista de alunos matriculados
def ver_dados_alunos():
    cabecalho("Lista de Alunos Matriculados")

    if not lista_de_alunos:
        print("Nenhum aluno matriculado!")
        return

    for aluno in lista_de_alunos:
        print(f"Matricula: {aluno["Matricula"]} | Nome: {aluno["Nome"]} | Curso: {aluno["Curso"]} | Periodo: {aluno["Periodo"]}")

#Atualizar matrícula (Melhorar a opção de quando colocar um número inválido!)
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
        print(f"\nAluno encontrado: {aluno_encontrado["Nome"]} Mátricula: {aluno_encontrado["Matricula"]}")
        print(" --- Insira os novos dados (Deixar em branco os que não quiser alterar! --- )")

        novo_nome = input(f"Novo nome: ({aluno_encontrado["Nome"]}): ")
        nova_idade = input(f"Nova Idade ({aluno_encontrado["Idade"]}): ")
        novo_genero = input(f"Novo Gênero: ({aluno_encontrado["Genero"]}): ")
        novo_curso = input(f"Novo Curso: ({aluno_encontrado["Curso"]}): ")
        novo_periodo = input(f"Novo Periodo ({aluno_encontrado["Periodo"]}): ")

        if novo_nome:
            aluno_encontrado["Nome"] = novo_nome
            
        if nova_idade:
            aluno_encontrado["Idade"] = nova_idade # Melhor seria adicionar validação aqui (se é número)
            
        if novo_genero:
            aluno_encontrado["Genero"] = novo_genero
        
        if novo_curso:
            aluno_encontrado["Curso"] = novo_curso
        
        if novo_periodo:
            aluno_encontrado["Periodo"] = novo_periodo
            
        print(f"\n Dados da matrícula {matricula_procurada} atualizados com sucesso!")
        
    else:
        print(f"\n Matrícula {matricula_procurada} não encontrada.")


def excluir_matricula():
    ver_dados_alunos()
    matricula_procurada = int(input("Digite o número de matricula que queira excluir: "))
    '''ver_dados_alunos()

    try:
        matricula_procurada = int(input("Digite o número de matricula que queira excluir: "))
        for aluno in lista_de_alunos:
            if aluno["Matricula"] == matricula_procurada:
                del aluno
                print(f"O aluno {aluno["Matricula"]} foi excluído da lista!")
                return
            else:
                print("Aluno não encontrado!")
    except ValueError:
        print("Matricula inválida!")'''
    
    aluno_removido = None # Inicializa a variável fora do loop (SOLUÇÃO 1)
    indice_a_deletar = -1

    for i, aluno in enumerate(lista_de_alunos):
        if aluno['Matricula'] == matricula_procurada:
            indice_a_deletar = i
            break
            
    if indice_a_deletar != -1:
        # AQUI garantimos que a variável 'aluno_removido' existe
        aluno_removido = lista_de_alunos.pop(indice_a_deletar)
        
        # SOLUÇÃO 2: Só imprime a mensagem se o aluno foi encontrado e removido
        print(f"✅ O aluno {aluno_removido['Nome']} foi excluído da lista!") 
        
    else:
        print(f"❌ Matrícula {matricula_procurada} não encontrada.")





        




# Código Principal
while True:
    cabecalho("Menu Principal")
    print("\n --- Selecione a opção desejada ---")
    print("1 - Matricular aluno")
    print("2 - Ler lista de matriculados")
    print("3 - Atualizar matricula")
    print("4 - Editar dados da matrícula")
    print("5 - Excluir matrícula")
    print("6 - Sair")

    opcao = input("\nSelecione a opção desejada: ")

    if opcao == "1":
        adicionar_alunos()
    
    elif opcao == "2":
        ver_dados_alunos()
    
    elif opcao == "3":
        atualizar_lista_alunos()

    elif opcao == "4":
        excluir_matricula()
        
    elif opcao == "5":
        print("Operação Finalizada!")
        break

    else:
        print("Valor inválido! Selecione outra opção: ")
    



    






'''
def ver_dados_alunos():

def atualizar_dados_alunos():



def exibir_menu_inicial():
# Exibir menu inicial

    while True:
        print("\n=\n"*30)
        print("\n ===== Selecione a opção desejada ===== ")
        print("\n1 - Matricular aluno")
        print("\n2 - Ler lista de matriculados")
        print("\n3 - Atualizar matricula")
        print("\n4 - Editar dados da matrícula")
        print("\n5 - Excluir matrícula")
        print("\n6 - Sair")
        print("\n=\n"*30)

        opcao = input("\nSelecione a opção desejada: ")

        if opcao == "1":
            def dados_necessarios_matricula():
                print("="*30)
                nome_aluno = input("\nDigite o nome do aluno: ")
                idade_aluno = input("\nDigite a idade do aluno: ")
                genero_aluno = input("\nDigite o gênero do aluno: ")
                turma_aluno = input("\nQual o ano escolar do aluno: ")

        
        elif opcao == "2":
            ver_dados_alunos():
        elif opcao == "3":

        elif opcao == "4":

        elif opcao == "5":

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Escolha novamente.")

        

        print("\n="*30)
'''