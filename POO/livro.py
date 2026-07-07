class Livro:
    def __init__(self, titulo, autor, reputacao):
        self.titulo = titulo
        self.autor = autor
        self.reputacao = reputacao

    def detalhes(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)

    def reputacao_livro(self):
        print("Reputação do livro:", self.reputacao)


livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Excelente, um clássico da literatura mundial.")


livro1.detalhes()
livro1.reputacao_livro()