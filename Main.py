todas_as_contas = []
op = 0
operacao = 0
LIMITE_SAQUE_DIARIO = 3
extrato = '### Extrato da Conta ###\n'

# Criar Conta / Usuário
def criar_usuario():
    print("### TELA DE CADASTRO DE USUARIO ###\n\n")
    
    nome = input("NOME: ")
    data_de_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF (Apenas 11 Digitos): ")
    endereco = input("Endereco (Logradouro - Bairro - Cidade/sigla estado): ")
    senha = input("Senha: ")
    
    print("\n")
    
    usuario = {"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco, "senha": senha}
    return usuario

def criar_conta():
    global todas_as_contas
    usuario = criar_usuario()

    if(verifica_cpf(usuario['cpf']) == 'tudo ok'):
        newConta = {"agencia": "0001", "saques_por_dia": 0, "numero_conta": len(todas_as_contas)+1, "saldo": 0, "usuario": usuario}
        todas_as_contas.append(newConta)
        print("Conta Criada com sucesso, Seja bem Vindo!")
    else:
        print(verifica_cpf(usuario['cpf']))

# Funções Úteis
def verifica_cpf(cpf):
    global todas_as_contas

    if(len(cpf) != 11):
        return 'CPF INVALIDO'

    for user in todas_as_contas:
        if(user['usuario']['cpf'] == cpf):
            return 'CPF JA EXISTE'

    return 'tudo ok'

def retorna_usuario(cpf, senha):
    for conta in todas_as_contas:
        if(conta['usuario']['cpf'] == cpf and conta['usuario']['senha'] == senha):
            return conta

def mostrar_usuarios():
    global todas_as_contas
    print("### TELA DE LISTAGEM DE USUARIOS ###\n")
    for user in todas_as_contas:
        print(user['usuario']['nome'])

# Login / Funções Logados

def Deposito(valor_para_depositar, conta):
    global extrato

    novoValor = conta['saldo'] + valor_para_depositar
    print(f"Valor depositado com sucesso!")
    
    operacao = f'R$ ' + str(float(valor_para_depositar))
    extrato += 'Depósito: ' + operacao + '\n'
    
    return novoValor

def Saque(valor_para_sacar, conta):
    global extrato

    if(valor_para_sacar <= conta['saldo'] and conta['saques_por_dia'] < 3):
        novoValor = conta['saldo'] - valor_para_sacar
        conta['saques_por_dia'] += 1

        print(f"Valor sacado com sucesso!")
        
        operacao = f'R$ ' + str(float(valor_para_sacar))
        extrato += 'Saque: ' + operacao + '\n'
        
        return novoValor
   
    elif valor_para_sacar > conta['saldo']:
        print("Voce nao tem saldo o suficiente para essa operação!\n")
   
    elif conta['saques_por_dia'] == 3:
        print("Você atingiu o limite máximo de saques por dia!\n")
    return conta['saldo']

def menu_logado(conta):
    global operacao, extrato

    while(operacao != 4):
        print("""
            ######## LOGIN ########
            [1] - Saque
            [2] - Depósito
            [3] - Verificar Extrato
            [4] - Sair do Programa
            ######################
        """)
        operacao = int(input("Qual operação você deseja fazer:"))

        if operacao == 1:    
            valor_para_sacar = float(input("Informe a quantia que deseja sacar: "))
            conta['saldo'] = Saque(valor_para_sacar, conta)

        elif operacao == 2:
            valor_para_depositar = float(input("Informe a quantia que deseja depositar: "))
            conta['saldo'] = Deposito(valor_para_depositar, conta)

        elif operacao == 3:
            copia = extrato
            copia += '\n\n' + 'Total: ' + str(float(conta['saldo']))
            print(copia)

        elif operacao == 4:
            print("Obrigado por usar nosso programa, até mais!\n")
        
        else:
            print("Operação informada nao existe!\n")

    operacao = 0
    extrato = '### Extrato da Conta ###\n'

def fazer_login():
    print("### TELA DE LOGIN DE USUARIO ###\n")
    
    cpf = input("Informe o seu CPF: ")
    senha = input("Informe a sua senha: ")
    
    print("\n")
        
    conta = retorna_usuario(cpf, senha)
    if(conta != None):
        menu_logado(conta)
    else:
        print("Valores informados estao incorretos!\n")

# Parte Inicial do Programa
while op != 4:
    print("""
        ######## MENU ########
        [1] - Login
        [2] - Cadastro
        [3] - Ver Usuários
        [4] - Sair do Programa
        ######################
    """)

    op = int(input("Qual operação você deseja fazer:"))

    if(op == 1):
        fazer_login()
    elif(op == 2):
        criar_conta()
    elif(op == 3):
        mostrar_usuarios()
    elif(op == 4):
        print("Até mais!")
    else:
        print("Opção invalida!")   
