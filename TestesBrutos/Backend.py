# Criar um aplicativo desktop para uma psicóloga

# 1. Cadastro de Pacientes
# Campos: Nome completo/ Data de nascimento/ Gênero/ CPF / RG/ Endereço/ Contato/ Nome do responsável (se menor de idade)/ Plano de saúde (se aplicável)
# Observações adicionais: Data do primeiro atendimento

# 2. Agenda / Calendário
# Visualização diária, semanal e mensal
# Marcar sessões com: Data e hora/ Duração/ Tipo (presencial, online)/ Status (agendada, realizada, cancelada, falta)/ Alertas / notificações/ Reagendamento com facilidade

# 3. Prontuário do Paciente
# Histórico de sessões/ Evolução do paciente (campo para texto livre)/ Diagnósticos (se aplicável)/ Estratégias de tratamento/ Anexos (áudios, PDFs, imagens — ex: laudos)/ Campo para resumo da sessão

# 4. Financeiro
# Controle por paciente e por data
# Campos: Valor da consulta/ Forma de pagamento (PIX, dinheiro, cartão, plano)/ Status (pago, pendente)/ Datas de pagamento/ Geração de recibo (PDF)/ Relatórios mensais/anuais

# 5. Relatórios
# Filtros por: Período/ Paciente/ Tipo de atendimento/ Status de pagamento/ Exportação: PDF / Excel

# 6. Login Seguro
# Login com senha/ Backup local ou na nuvem (criptografado)/ Criptografia de dados sensíveis

class Paciente:
    def __init__(self, name, age): # birthday, gender, CPF, RG, adress, contact, id):
        self.name = name
        self.age = age
        # self.birthday = birthday
        # self.gender = gender
        # self.CPF = CPF
        # self.RG = RG
        # self.adress = adress
        # self.contact = contact
        # self.id = id

    def addInfo(self, FirstSession):
        self.FirstSession = FirstSession

    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}"
        # Data de Nascimento: {self.birthday}, Gênero: {self.gender}, CPF: {self.name}, RG: {self.RG}, Endereço: {self.adress}, Contato: {self.contact}, Data da primeira sessão: {self.FirstSession}, ID: {self.id}"

class session:
    def __init__(self, date, hour, duration, type, status, content):
        self.date = date
        self.hour = hour
        self.duration = duration
        self.type = type
        self.status = status
        self.content = content

    def __str__(self):
        return f"Data: {self.date}, Horário: {self.hour}, Conteúdo: {self.content}"

def create():
    name = input("Insira o nome do paciente: ")
    age = input("Insira a idade do Paciente: ")
    paciente = Paciente(name, age)

    with open (f"./TestesBrutos/Data/Paciente_{name}", "w", encoding="utf-8") as patient:
        patient.write(f"{str(paciente)}")
        
def read():
    pass

def update():
    pass
    
def remove():
    pass

def error():
    print("Opção inválida.")


Menu = {
    1: create,
    2: read,
    4: update,
    3: remove
}

print("\n1.Criar novo paciente  " \
      "\n2.Ler o prontuário " \
      "\n3.Atualizar o prontuário " \
      "\n4.Excluir algum paciente \n")

option = int(input("Selecione a opção desejada: "))
Menu.get(option, error)()