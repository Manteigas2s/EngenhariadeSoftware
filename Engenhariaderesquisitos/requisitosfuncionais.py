class BancoContato():
    def __init__(self):
        self.contatos = []
        self.id_contato = 1    

    def Menu(self):
        while True:

            print("=" * 45)
            print(" SISTEMA DE CADASTRO DE CONTATOS ")
            print("=" * 45)
            print("1 - Cadastrar contato")
            print("2 - Listar contatos")
            print("3 - Editar contato")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.cadastro_contatos()

            elif opcao == "2":
                self.listar_contatos()
            
            elif opcao == "3":
                self.editar_contatos()

            elif opcao == "0":
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inválida!\n")

    def Login(self):
        usuario_correto = "Admin"
        senha_correta = "1234"
        
        print("=" * 45)
        print("        LOGIN DO SISTEMA")
        print("=" * 45)

        while True:
            usuario = input("Usuário: ").strip()
            senha = input("Senha: ")

            if usuario_correto == usuario and senha_correta == senha:
                print("Login feito com sucesso!")
                break
            else:
                print("Usuário ou senha incorretos!")
                print("Tente novamente!")
                

    def cadastro_contatos(self):

        print("\n========== CONTATO CADASTRADO ==========")

        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        empresa = input("Empresa: ").strip()
        
        if nome == "" or telefone == "" or email == "" or empresa == "":
            print("\nTodos os campos são obrigatórios!")
            print("Tente novamente.\n")
            return
        
        contato = {
            "ID": self.id_contato,
            "Nome":nome,
            "Telefone":telefone,
            "Email":email,
            "Empresa":empresa

        }
        self.contatos.append(contato)
        self.id_contato += 1

        print("Contato cadastrado com sucesso!")

    def listar_contatos(self):
        print("\n========== LISTA DE CADASTRADOS ==========")
        
        if len(self.contatos) == 0:
            print("Nenhum contato cadastrado.")
            return
    
        for contato in self.contatos:
            print(f"""
    ID: {contato['ID']}
    Nome: {contato['Nome']}
    Telefone: {contato['Telefone']}
    Email: {contato['Email']}
    Empresa: {contato['Empresa']}
    ----------------------------------
    """)
            
    def editar_contatos(self):
        print("\n========== CONTATOS CADASTRADOS ==========")
        if len(self.contatos) == 0:
            print("\nNenhum contato cadastrado.")
            print("Faça um cadastro primeiro.")
            return
        
        try:
            id_editar = int(input("Informe o ID do contato: "))
        except ValueError:
            print("ID inválido!")
            return

        for contato in self.contatos:
            if contato['ID'] == id_editar:
                print("\nContato encontrado!")

                novo_nome = input(f"Nome ({contato['Nome']}): ").strip()
                if novo_nome != "":
                    contato["Nome"] = novo_nome

                novo_telefone = input(f"Telefone ({contato['Telefone']}): ").strip()
                if novo_telefone != "":
                    contato["Telefone"] = novo_telefone
                
                novo_email = input(f"Email ({contato['Email']}): ").strip()
                if novo_email != "":
                    contato["Email"] = novo_email

                nova_empresa = input(f"Empresa ({contato['Empresa']}): ").strip()
                if nova_empresa != "":
                    contato["Empresa"] = nova_empresa

                print("\nContato atualizado com sucesso!")
                return
        
        print("\nContato não encontrado.")
        print("Cadastre o contato primeiro.")
        

sistema = BancoContato()
sistema.Login()
sistema.Menu()

