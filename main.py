import subprocess

def cabecalho(msg):
    """Exibe um cabeçalho formatado"""
    tam = len(msg) + 4
    print("\n" + "=" * tam)
    print(f"  {msg}")
    print("=" * tam)

def main():
    """Menu principal que chama cada sistema"""
    python_cmd = "python3"
    
    while True:
        cabecalho("GESTÃO ESCOLAR COMUNITÁRIA")
        print("\n1 - Gestão de Alunos")
        print("2 - Gestão de Professores")
        print("3 - Gestão de Turmas")
        print("4 - Relatório de Integração")
        print("5 - Sair do Sistema")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n Iniciando sistema de Alunos...")
            subprocess.run([python_cmd, "modulos/alunos/crud_alunos.py"])
            
        elif opcao == "2":
            print("\n Iniciando sistema de Professores...")
            subprocess.run([python_cmd, "modulos/professores/crud_professores.py"])
            
        elif opcao == "3":
            print("\n Iniciando sistema de Turmas...")
            subprocess.run([python_cmd, "modulos/turmas/crud_turmas.py"])
            
        elif opcao == "4":
            print("\n Gerando Relatório de Integração...")
            subprocess.run([python_cmd, "relatorio_integracao.py"])
            
        elif opcao == "5":
            print("\n Encerrando o sistema...")
            print("Até logo!")
            break
            
        else:
            print("\n Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
