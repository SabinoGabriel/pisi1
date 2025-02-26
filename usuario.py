def validar_email(email):
    return '@' in email and '.' in email

def validar_cpf(cpf):
    cpf_list = []
    if len(cpf) != 11:
        return False

    for i in cpf:
        cpf_list.append(int(i))

    def calcular_soma(indice_inicial):
        soma = 0
        multiplier = 2
        for i in range(indice_inicial, -1, -1):
            soma += cpf_list[i] * multiplier
            multiplier += 1
        return soma

    soma_1 = calcular_soma(8)
    remainder_1 = soma_1 % 11
    digit_1 = 0 if remainder_1 < 2 else 11 - remainder_1
    if digit_1 != cpf_list[9]:
        return False

    soma_2 = calcular_soma(9)
    remainder_2 = soma_2 % 11
    digit_2 = 0 if remainder_2 < 2 else 11 - remainder_2
    if digit_2 != cpf_list[10]:
        return False

    return True

def criar_conta(usuarios):
    email = input('Digite seu email:\n').strip()
    while not validar_email(email):
        print('Email inválido! Tente novamente.')
        email = input('Digite seu email:\n').strip()
    
    cpf = input('Digite seu CPF:\n').strip()
    while not validar_cpf(cpf):
        print('CPF inválido! Tente novamente.')
        cpf = input('Digite seu CPF:\n').strip()

    senha = input('Digite sua senha (mínimo 6 caracteres):\n').strip()
    while len(senha) < 6:
        print('Senha muito curta! Tente novamente.')
        senha = input('Digite sua senha (mínimo 6 caracteres):\n').strip()
    
    # Verificar se o email ou CPF já estão cadastrados
    email_ja_cadastrado = any(user['cpf'] == cpf or user['email'] == email for user in usuarios.values())
    if email_ja_cadastrado:
        print('Usuário já cadastrado com este email ou CPF!')
    else:
        usuarios[email] = {
            "cpf": cpf,
            "senha": senha,
            "estado": {
                "pensamentos": [],
                "pensamento_diario": None,
                "descanso": False,
                "data": None,
                "aux_list": [],
                "sample": []
            }
        }
        usuarios[cpf] = usuarios[email]
        print('Conta criada com sucesso!')
    return usuarios

def fazer_login(usuarios):
    identificador = input('Digite seu email ou CPF:\n').strip()
    senha = input('Digite sua senha:\n').strip()

    if '@' in identificador:
        usuario = usuarios.get(identificador)
    else:
        usuario = next((user for user in usuarios.values() if user['cpf'] == identificador), None)
    

    if usuario and usuario['senha'] == senha:
        print('Login efetuado com sucesso!')
        return usuario['estado']
    else:
        print('Email/CPF ou senha incorretos!')
        return None