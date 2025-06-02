import os

class Paciente:
    def __init__(self, name, age, civil_status, profession): # birthday, gender, CPF, RG, adress, contact, id):
        self.name = name
        self.age = age
        self.civil_status = civil_status
        self.profession = profession
        # self.birthday = birthday
        # self.gender = gender
        # self.CPF = CPF
        # self.RG = RG
        # self.adress = adress
        # self.contact = contact
        # self.id = id

    def addInfo(self, GuardianName):
        self.GuardianName = GuardianName
        return f"Nome do responsável: {self.GuardianName}"

    def __str__(self):
        return f"Nome: {self.name} \nIdade: {self.age} \nEstado Civil: {self.civil_status} \nProfissão: {self.profession}"
        # Data de Nascimento: {self.birthday}, Gênero: {self.gender}, CPF: {self.name}, RG: {self.RG}, Endereço: {self.adress}, Contato: {self.contact}, Data da primeira sessão: {self.FirstSession}, ID: {self.id}"

class Session:
    def __init__(self, date, hour, queixa_principal, historico_familiar, historico_pessoal, aspectos, obs): #, duration, type, status, queixa_principal)
        self.date = date
        self.hour = hour
        # self.duration = duration
        # self.type = type
        # self.status = status
        self.queixa_principal = queixa_principal
        self.historico_familiar = historico_familiar
        self.historico_pessoal = historico_pessoal
        self.aspectos = aspectos
        self.obs = obs

    def __str__(self):
        return f"Data: {self.date}, Horário: {self.hour}\n\nQueixa Principal: {self.queixa_principal} \n\nHistórico Familiar: {self.historico_familiar} \n\nHistórico Pessoal: {self.historico_pessoal} \n\nAspectos emocionais e comportamentais: {self.aspectos} \n\nObservações: {self.obs}"
 
def create():
    name = input("Insira o nome do paciente: ")
    age = int(input("Insira a idade do Paciente: "))
    civil_status = input("Estado Cívil do paciente: ")
    profession = input("Insira a profissão do paciente: ")
    paciente = Paciente(name, age, civil_status, profession)
    date = input("Insira a data do atendimento: ")
    hour = input("Insira o horário da sessão: ")
    queixa_principal = input("Queixa principal: ")
    historico_familiar = input("Histórico Familiar: ")
    historico_pessoal = input("Histórico Pessoal: ")
    aspectos = input("Aspectos emocionais e comportamentais: ")
    obs = input("Observações: ")
    session = Session(date, hour, queixa_principal, historico_familiar, historico_pessoal, aspectos, obs)

    if age < 18:
        GuardianName = input("Qual o nome do responsável: ")
        guardian = paciente.addInfo(GuardianName)
        with open (f"./TestesBrutos/Data/Paciente_{name}", "w", encoding="utf-8") as patient:
            patient.write(f"{str(paciente)}\n{str(guardian)}\n{str(session)}")
    else:
        with open (f"./TestesBrutos/Data/Paciente_{name}", "w", encoding="utf-8") as patient:
            patient.write(f"{str(paciente)}\n{str(session)}")
        
def read():
    name = input("Insira o nome do paciente: ")
    with open (f"./TestesBrutos/Data/Paciente_{name}", "r", encoding="utf-8") as patient:
        patient = patient.readlines()
        for i in patient:
            print(i, end="")
  

def update():
    name = input("Insira o nome do paciente: ")
    with open (f"./TestesBrutos/Data/Paciente_{name}", "r", encoding="utf-8") as patient:
        patient = patient.readlines()
        for i in patient:
            print(i, end="")
    
    queixa_principal = input("\nDigite o conteúdo da Alteração: \n")
    with open (f"./TestesBrutos/Data/Paciente_{name}", "a", encoding="utf-8") as patient:
        patient.write(f"\n{str(queixa_principal)}\n")
# 
def remove():
    name = input("Insira o nome do paciente: ")
    file = f"./TestesBrutos/Data/Paciente_{name}"
    if os.path.exists(file):
        os.remove(file)
    else:
        print("O arquivo não existe.")

def invalid():
    print("Opção inválida.")


Menu = {
    1: create,
    2: read,
    3: update,
    4: remove
}

os.system('cls')

while True:
    print("\n----- Gerenciamento de Pacientes -----")
    print("\n1.Criar novo paciente  " \
        "\n2.Ler o prontuário " \
        "\n3.Atualizar o prontuário " \
        "\n4.Excluir algum paciente" \
        "\n5.Sair \n")

    option = int(input("Selecione a opção desejada: "))
    if option == 5:
        break
    Menu.get(option, invalid)()