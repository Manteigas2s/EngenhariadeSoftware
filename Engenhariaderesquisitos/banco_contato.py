from contato import Contato


class BancoContato:

    def __init__(self):
        self.contatos = []
        self.id_contato = 1

    def cadastro_contatos(self):

        print("\n========== CADASTRAR CONTATO ==========")

        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        empresa = input("Empresa: ").strip()

        if not nome or not telefone or not email or not empresa:
            print("\nTodos os campos são obrigatórios!")
            return

        contato = Contato(
            self.id_contato,
            nome,
            telefone,
            email,
            empresa
        )

        self.contatos.append(contato)
        self.id_contato += 1

        print("\nContato cadastrado com sucesso!")

    def listar_contatos(self):

        print("\n========== LISTA DE CONTATOS ==========")

        if not self.contatos:
            print("Nenhum contato cadastrado.")
            return

        contatos_ordenados = sorted(
            self.contatos,
            key=lambda contato: contato.nome.lower()
        )

        for contato in contatos_ordenados:
            print(f"""
ID: {contato.id}
Nome: {contato.nome}
Telefone: {contato.telefone}
Email: {contato.email}
Empresa: {contato.empresa}
----------------------------------
""")

    def editar_contatos(self):

        if not self.contatos:
            print("\nNenhum contato cadastrado.")
            return

        self.listar_contatos()

        try:
            id_editar = int(input("Informe o ID: "))
        except ValueError:
            print("ID inválido.")
            return

        for contato in self.contatos:

            if contato.id == id_editar:

                nome = input(f"Nome ({contato.nome}): ").strip()
                telefone = input(f"Telefone ({contato.telefone}): ").strip()
                email = input(f"Email ({contato.email}): ").strip()
                empresa = input(f"Empresa ({contato.empresa}): ").strip()

                if nome:
                    contato.nome = nome

                if telefone:
                    contato.telefone = telefone

                if email:
                    contato.email = email

                if empresa:
                    contato.empresa = empresa

                print("\nContato atualizado!")
                return

        print("\nContato não encontrado.")

    def excluir_contatos(self):

        if not self.contatos:
            print("\nNenhum contato cadastrado.")
            return

        self.listar_contatos()

        try:
            id_excluir = int(input("Informe o ID: "))
        except ValueError:
            print("ID inválido.")
            return

        for contato in self.contatos:

            if contato.id == id_excluir:

                confirmar = input(
                    f"Deseja excluir {contato.nome}? (S/N): "
                ).upper()

                if confirmar == "S":
                    self.contatos.remove(contato)
                    print("Contato excluído!")

                return

        print("Contato não encontrado.")

    def pesquisar_contatos(self):

        if not self.contatos:
            print("\nNenhum contato cadastrado.")
            return

        pesquisa = input(
            "\nDigite o nome, telefone ou email: "
        ).strip().lower()

        encontrado = False

        for contato in self.contatos:

            if (pesquisa == contato.nome.lower()
                    or pesquisa == contato.telefone
                    or pesquisa == contato.email.lower()):

                print(f"""
ID: {contato.id}
Nome: {contato.nome}
Telefone: {contato.telefone}
Email: {contato.email}
Empresa: {contato.empresa}
----------------------------------
""")

                encontrado = True

        if not encontrado:
            print("Nenhum contato encontrado.")