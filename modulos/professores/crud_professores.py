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
                    print(f"Professor {prof_deletar} removido com sucesso.")
                    continue
                else:
                    print(f"\nProfessor {prof_deletar} não encontrado.....")
                    print("Err0r...")
        case 3:
            print("\n ----- CONSULTA DE PROFESSORES -----")
            
            if not professor:
                print(" Ops! Nossa base de dados está vazia por enquanto.")
                print("Dica: Vá na opção 1 para cadastrar alguém.")
            else:
                print(f"Encontrei {len(professor)} professor(es) cadastrado(s):")
                for i, prof in enumerate(professor):
                    print(f"\n Ficha do Professor #{i+1}")
                    print(f"   Nome:    {prof.get('nome', 'Sem nome')}")
                    print(f"   Idade:   {prof.get('idade', 'Não informada')}")
                    print(f"   Matéria: {prof.get('materia', 'Não informada')}")
                    print("   " + "-"*30) 

            print("\n------------------------------------------------")
            cnt = input("Gostaria de realizar outra operação? [S]im / [N]ão: ").lower()
            if cnt == "n":
                print("\nObrigado por usar o sistema! Até a próxima. ")
                break
            elif cnt == "s": 
                continue
            else:
                print("Não entendi, mas vou te levar de volta ao menu principal.")

        case 4:
            print("\n ----- ATUALIZAÇÃO DE DADOS -----")
            prof_atualizar = input("Qual o nome do professor que você quer editar? ")
            encontrado = False
            
            for prof in professor:
                if prof['nome'].lower() == prof_atualizar.lower():
                    encontrado = True
                    print(f"\n Achei! Vamos editar os dados de: {prof['nome']}")
                    print(" DICA: Pressione ENTER vazio se não quiser mudar o valor atual.")
                
                    novo_nome = input(f"   Novo Nome (Atual: {prof['nome']}): ")
                    if novo_nome:
                        prof['nome'] = novo_nome

                    nova_idade = input(f"   Nova Idade (Atual: {prof['idade']}): ")
                    if nova_idade:
                        try:
                            prof['idade'] = int(nova_idade)
                        except ValueError:
                            print("     Ops, idade precisa ser número. Mantive a antiga.")

                    nova_materia = input(f"   Nova Matéria (Atual: {prof['materia']}): ")
                    if nova_materia:
                        prof['materia'] = nova_materia

                    salvar_professores(professor)
                    print("\n Sucesso! As informações foram atualizadas.")
                    break 
            
            if not encontrado:
                print(f"Poxa, não encontrei ninguém com o nome '{prof_atualizar}'.")

            print("\n------------------------------------------------")
            cnt = input("Gostaria de realizar outra operação? [S]im / [N]ão: ").lower()
            if cnt == "n":
                print("\nObrigado por usar o sistema! Até a próxima. 👋")
                break
            elif cnt == "s": 
                continue
            else:
                print("Não entendi, mas vou te levar de volta ao menu principal.")

        case 5:
            print("\n Encerrando o sistema... Tenha um bom dia!")
            break

        case _:
            print("\n Essa opção não existe. Por favor, escolha um número entre 1 e 5.")