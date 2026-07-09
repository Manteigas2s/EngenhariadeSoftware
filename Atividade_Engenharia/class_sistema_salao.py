class Agendamento:
    def __init__(self, cliente, servico, data, horario):
        self.cliente = cliente
        self.servico = servico
        self.data = data
        self.horario = horario

class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

class Servico:
    def __init__(self, nome, valor, duracao):
        self.nome = nome
        self.valor = valor
        self.duracao = duracao