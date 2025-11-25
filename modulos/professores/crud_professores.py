import json
import os 


diretorio_script = os.path.dirname(os.path.abspath(__file__))
professor = [] 
armaze_prof = os.path.join(diretorio_script, 'professores.json')


def carregar_professores():
    if os.path.exists(armaze_prof):
        try:
            with open(armaze_prof, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            print("Aviso: Arquivo de dados JSON vazio ou inválido. Iniciando com lista vazia.")
            return []
    return []

def salvar_professores(lista_professores):
    try:
        with open(armaze_prof, 'w', encoding='utf-8') as f:
            json.dump(lista_professores, f, indent=4, ensure_ascii=False) 
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")



def menu():
    print("---------SISTEMA OPERACIONAL----------")
    print("\n1- Adicionar professor..")
    print("2- Deletar professor..")
    print("3- Listar professores..")
    print("4- Atualizar professroes..")
    print("5- SAIR DO SISTEMA")
    escolha = int(input("\nEscolha oque voce quer fazer de acordo com a numeração: "))
    return escolha


professor = carregar_professores() 

while True:
    match (menu()):
        
        case 1:
            print("sistema: ADD PROFESSOR...")
            nome= input("\nDigite o nome desse professor: ")
            turno = input("Digite sue turno: ")
            materia = input("Digite a area que ele atua: ")
            prof = {
                'nome': nome,
                'turno': turno,
                'materia': materia
            }
        

            professor.append(prof)
            salvar_professores(professor)

            print ("\n ----- Dados do Professor Adicionado -----")
            print(f"Nome: {prof['nome']}")
            print(f"Turno: {prof['turno']}")
            print(f"Materia: {prof['materia']}")
            print("\n PROFESSOR ADICIONADO!!!!")

            
            cnt = input("Voce deseja continuar (S/N):")
            if cnt == "n":
                print("Fechando sistema....")
                break
            elif cnt == "s": 
                continue
            else:
                print("Er00r...")

        case 2:
            print("sistema: DELETE PROFESSOR...")
            prof_deletar = input("\nDigite o nome do professor que voçe quer retirar do sitema: ")
            for prof in professor:
                if prof['nome'].lower() == prof_deletar.lower():
                    professor.remove(prof)
                    salvar_professores(professor)
                    print("----RESUMO DO PROF----")
                    print(f"Nome: {prof['nome']}")
                    print(f"Turno: {prof['turno']}")
                    print(f"Materia: {prof['materia']}")
                    print("-----------------------------")
                    print(f"Professor {prof_deletar} removido com sucesso.")
                    continue
                else:
                    print(f"\nProfessor {prof_deletar} não encontrado.....")
                    print("Err0r...")
        case 3:
            print("\n----- SISTEMA: LISTAR PROFESSORES -----")
            print(f"[DEBUG] Conteúdo da lista: {professor}") 
            
            if not professor:
                print("Nenhum professor cadastrado (Lista Vazia).")
            else:
                for i, prof in enumerate(professor):
                    print(f"\nPROFESSOR #{i+1}")
                    print(f"Nome: {prof.get('nome', 'N/A')}")
                    print(f"Turno: {prof.get('turno', 'N/A')}")
                    print(f"Matéria: {prof.get('materia', 'N/A')}")
                    print("-----------------------------")

            cnt = input("\nVoce deseja continuar (S/N): ").lower()
            if cnt == "n":
                print("Fechando sistema....")
                break
            elif cnt == "s": 
                continue
            else:
                print("Opção inválida. Voltando ao menu.")

        case 4:
            print("\n----- SISTEMA: ATUALIZAR PROFESSOR -----")
            prof_atualizar = input("Digite o nome do professor que deseja atualizar: ")
            encontrado = False
            
            for prof in professor:
                if prof['nome'].lower() == prof_atualizar.lower():
                    encontrado = True
                    print(f"\nProfessor {prof['nome']} encontrado.")
                    print("Digite os novos dados (ou aperte ENTER para manter o atual):")
                    
                    novo_nome = input(f"Novo Nome ({prof['nome']}): ")
                    if novo_nome:
                        prof['nome'] = novo_nome

                    nova_turno = input(f"Novo Turno ({prof['turno']}): ")
                    if nova_turno:
                        try:
                            prof['turno'] = (nova_turno)
                        except ValueError:
                            print("Erro: o turno não pode ser um número.")

                    nova_materia = input(f"Nova Matéria ({prof['materia']}): ")
                    if nova_materia:
                        prof['materia'] = nova_materia

                    salvar_professores(professor)
                    print("\nProfessor atualizado com sucesso!")
                    break 
            
            if not encontrado:
                print(f"Professor '{prof_atualizar}' não encontrado.")

            cnt = input("\nVoce deseja continuar (S/N): ").lower()
            if cnt == "n":
                print("Fechando sistema....")
                break
            elif cnt == "s": 
                continue
            else:
                print("Opção inválida. Voltando ao menu.")

        case 5:
            print("\nFECHANDO SISTEMA....")
            break

        case _:
            print("\nOpção inválida. Digite um número de 1 a 5.")   
