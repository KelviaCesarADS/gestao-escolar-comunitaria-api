professor = []

def menu():
    print("---------SISTEMA OPERACIONAL----------")
    print("\n1- Adicionar professor..")
    print("2- Deletar professor..")
    print("3- Listar professores..")
    print("4- Atualizar professroes..")
    print("5- SAIR DO SISTEMA")
    escolha = int(input("\nEscolha oque voce quer fazer de acordo com a numeração: "))
    return escolha


while True:
    match (menu()):
        case 1:
            prof = {}
            print("sistema: ADD PROFESSOR...")
            prof["nome"] = input("\nDigite o nome desse professor: ")
            prof["idade"] = int(input("Digite sua idade: "))
            prof["materia"] = input("Digite a area que ele atua: ")
            professor.append(prof)

            print ("\n ----- Dados dos Alunos -----")
            print(f"Nome: {prof['nome']}")
            print(f"Idade: {prof['idade']}")
            print(f"Materia: {prof['materia']}")
            print("\n PROFESSOR ADICIONADO!!!!")

            
            cnt = input("Voce deseja continuar (S/N):")
            if cnt == "n" or "N":
                print("Fechando sistema....")
                break
            elif cnt == "S" or "s":
                continue
            else:
              print("Er00r...")
