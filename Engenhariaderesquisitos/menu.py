from banco_contato import BancoContato


class Menu:

    def __init__(self):
        self.banco = BancoContato()

    def iniciar(self):

        while True:

            print("\n" + "=" * 45)
            print(" SISTEMA DE CADASTRO DE CONTATOS ")
            print("=" * 45)
            print("1 - Cadastrar contato")
            print("2 - Listar contatos")
            print("3 - Editar contato")
            print("4 - Excluir contato")
            print("5 - Pesquisar contato")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.banco.cadastro_contatos()

            elif opcao == "2":
                self.banco.listar_contatos()

            elif opcao == "3":
                self.banco.editar_contatos()

            elif opcao == "4":
                self.banco.excluir_contatos()

            elif opcao == "5":
                self.banco.pesquisar_contatos()

            elif opcao == "0":
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inválida!")