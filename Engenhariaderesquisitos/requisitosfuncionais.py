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
            print("4 - Excluir contato")
            print("5 - Pesquisar contato")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.cadastro_contatos()

            elif opcao == "2":
                self.listar_contatos()
            
            elif opcao == "3":
                self.editar_contatos()

            elif opcao == "4":
                self.excluir_contatos()

            elif opcao == "5":
                self.pesquisar_contatos()
                
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
        
        # Sorted usado para organizar em ordem alfabética
        contatos_ordenados = sorted(
            self.contatos,
            key=lambda contato: contato["Nome"].lower()
        )

        for contato in contatos_ordenados:
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
        
        for contato in self.contatos:
            print(f"""
    ID: {contato['ID']}
    Nome: {contato['Nome']}
    Telefone: {contato['Telefone']}
    Email: {contato['Email']}
    Empresa: {contato['Empresa']}
    ----------------------------------
    """)
            
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
    
    def excluir_contatos(self):
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
            
        try:
            id_excluir = int(input("Informe o ID do contato: "))
        except ValueError:
            print("ID inválido!")
            return
        
        for contato in self.contatos:
            if contato['ID'] == id_excluir:
                print(f"\nContato encontrado!: {contato['Nome']}")

                confirmar = input("Deseja realmente excluir? (S/N): ").upper()

                if confirmar == "S":
                    self.contatos.remove(contato)
                    print("Contato excluído com sucesso!")
                else:
                    print("Exclusão concluída!")
                return
        print("Contato não encontrado")

    def pesquisar_contatos(self):
        print("\n========== PESQUISAR CONTATO ==========")

        if len(self.contatos) == 0:
            print("Nenhum contato cadastrado.")
            return

        pesquisa = input("Digite o nome, telefone ou e-mail: ").strip().lower()

        encontrado = False

        for contato in self.contatos:

            if (pesquisa == contato["Nome"].lower() or
                pesquisa == contato["Telefone"] or
                pesquisa == contato["Email"].lower()):

                print(f"""
        ID: {contato['ID']}
        Nome: {contato['Nome']}
        Telefone: {contato['Telefone']}
        Email: {contato['Email']}
        Empresa: {contato['Empresa']}
        ----------------------------------
        """)
                encontrado = True

        if not encontrado:
            print("\nNenhum contato encontrado.")

sistema = BancoContato()
sistema.Login()
sistema.Menu()

