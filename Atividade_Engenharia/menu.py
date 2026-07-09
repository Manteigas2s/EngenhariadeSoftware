from sistema_salao import SistemaSalao

class Menu:

    def __init__(self):
        self.banco = SistemaSalao()

    def iniciar(self):

        while True:

            print("\n" + "=" * 45)
            print(" SALÃO DE BELEZA ")
            print("=" * 45)
            print("1 - Cadastrar cliente")
            print("2 - Cadastrar serviço")
            print("3 - Agendar atendimento")
            print("4 - Listar agendamentos")
            print("5 - Cancelar agendamento")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.banco.cadastro_clientes()

            elif opcao == "2":
                self.banco.cadastro_servicos()

            elif opcao == "3":
                self.banco.agendar_servico()

            elif opcao == "4":
                self.banco.listar_agendamentos()

            elif opcao == "5":
                self.banco.cancelar_agendamento()

            elif opcao == "0":
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inválida!")