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
            idade = int(input("Digite sua idade: "))
            materia = input("Digite a area que ele atua: ")
            prof = {
                'nome': nome,
                'idade': idade,
                'materia': materia
            }
        
            professor.append(prof)
            salvar_professores(professor)

            print ("\n ----- Dados do Professor Adicionado -----")
            print(f"Nome: {prof['nome']}")
            print(f"Idade: {prof['idade']}")
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
                    print(f"Idade: {prof['idade']}")
                    print(f"Materia: {prof['materia']}")
                    print("-----------------------------")
                    print(f"\nProfessor {prof_deletar} removido com sucesso.")
                    continue
                else:
                    print(f"\nProfessor {prof_deletar} não encontrado.....")
                    print("Err0r...")
                    



