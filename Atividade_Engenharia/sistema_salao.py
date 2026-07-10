from class_sistema_salao import Agendamento, Servico, Cliente


class SistemaSalao:
    def __init__(self):
        self.clientes = []
        self.servicos = []
        self.agendamentos = []

    def cadastro_clientes(self):
        while True:
            nome = input("Nome: ").strip()
            if not nome:
                print("Preenchemento obrigatório!")
                continue
            cpf = input("CPF: ").strip()
            if not cpf:
                print("CPF obrigatório!")
                continue

            if any(cliente.cpf == cpf for cliente in self.clientes):
                print("CPF já cadastrado!")
                continue
            
            telefone = input("Telefone: ").strip()
            if not telefone:
                print("Telefone é obrigatório!")
                continue

            email = input("Email: ").strip()
            if not email:
                print("Email é obrigatório!")
                continue

            cliente = Cliente(
                nome,
                cpf,
                telefone,
                email,
                
            )

            self.clientes.append(cliente)
            print("\nContato cadastrado com sucesso!")
            break

    def cadastro_servicos(self):
        while True: 
            nome = input("Nome do serviço: ").strip()
            if not nome:
                print("Nome do serviço é obrigatório!")

            if any(servico.nome.lower() == nome.lower() for servico in self.servicos):
                print("Esse serviço já está cadastrado!")
                continue

            try:
                valor = float(input("Valor: R$ ").replace(",", "."))
                duracao = int(input("Duração (em minutos): "))
            except ValueError:
                print("Valor ou duração inválidos!")
                continue

            if valor <= 0 or duracao <= 0:
                print("Valor e Duração deve ser maior que zero!")
                continue

            servico = Servico(nome, valor, duracao)
            self.servicos.append(servico)

            print("Serviço cadastrado com sucesso!")
            break

    def agendar_servico(self):
        cpf = input("CPF do cliente: ").strip()

        cliente = None
        for c in self.clientes:
            if c.cpf == cpf:
                cliente = c
                break

        if cliente is None:
            print("Cliente não encontrado!")
            return

        nome_servico = input("Nome do serviço: ").strip()

        servico = None
        for s in self.servicos:
            if s.nome.lower() == nome_servico.lower():
                servico = s
                break

        if servico is None:
            print("Serviço não encontrado!")
            return

        data = input("Data (dd/mm/aaaa): ").strip()
        horario = input("Horário (HH:MM): ").strip()

        for agendamento in self.agendamentos:
            if agendamento.data == data and agendamento.horario == horario:
                print("Já existe um agendamento nesse horário!")
                return

        agendamento = Agendamento(cliente, servico, data, horario)
        self.agendamentos.append(agendamento)

        print("Agendamento realizado com sucesso!")

    def listar_agendamentos(self):
        if not self.agendamentos:
            print("Nenhum agendamento cadastrado!")
            return

        print("\n===== AGENDAMENTOS =====")

        for i, agendamento in enumerate(self.agendamentos, start=1):
            print(f"\nAgendamento {i}")
            print(f"Cliente : {agendamento.cliente.nome}")
            print(f"Serviço : {agendamento.servico.nome}")
            print(f"Data    : {agendamento.data}")
            print(f"Horário : {agendamento.horario}")

    def cancelar_agendamento(self):
        cpf = input("CPF do cliente: ").strip()
        data = input("Data do agendamento (dd/mm/aaaa): ").strip()
        horario = input("Horário do agendamento (HH:MM): ").strip()

        agendamento_encontrado = None

        for agendamento in self.agendamentos:
            if (agendamento.cliente.cpf == cpf and
                agendamento.data == data and
                agendamento.horario == horario):
                agendamento_encontrado = agendamento
                break

        if agendamento_encontrado is None:
            print("Agendamento não encontrado!")
            return

        confirmar = input("Confirmar cancelamento? (S/N): ").upper()

        if confirmar == "S":
            self.agendamentos.remove(agendamento_encontrado)
            print("Agendamento cancelado com sucesso!")
        else:
            print("Cancelamento cancelado.")
