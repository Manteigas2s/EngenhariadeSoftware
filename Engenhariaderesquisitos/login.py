class Login:

    def autenticar(self):
        usuario_correto = "Admin"
        senha_correta = "1234"

        print("=" * 45)
        print("        LOGIN DO SISTEMA")
        print("=" * 45)

        while True:
            usuario = input("Usuário: ").strip()
            senha = input("Senha: ")

            if usuario == usuario_correto and senha == senha_correta:
                print("\nLogin realizado com sucesso!\n")
                return True

            print("\nUsuário ou senha incorretos!")
            print("Tente novamente.\n")