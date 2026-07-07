class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def __str__(self):
        return f"Aluno {self.nome} esta regulamente matriculado com a matricula {self.matricula}"
    
    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Matrícula:", self.matricula)
        print("Nota:", self.nota)

    def aprov_repro(self, notas):
        self.notas.extend(notas)
        if sum(self.notas) / len(self.notas) >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
        
aluno1 = Aluno("Everton", 1234)

print(aluno1)
print(f"{aluno1} e esta {aluno1.aprov_reprov(10, 8, 9)}")

aluno1.exibir_informacoes()
aluno1.aprovado_reprovado()