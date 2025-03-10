def validar_email(email):
    return '@' in email and '.' in email

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 0 if soma % 11 < 2 else 11 - soma % 11
    if digito1 != int(cpf[9]):
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 0 if soma % 11 < 2 else 11 - soma % 11
    return digito2 == int(cpf[10])

def criar_conta(usuarios, contador_id):
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
    
    email_ja_cadastrado = False
    for user in usuarios.values():
        if user['cpf'] == cpf or user['email'] == email:
            email_ja_cadastrado = True
            break

    if email_ja_cadastrado:
        print('Usuário já cadastrado com este email ou CPF!')
    else:
        id = str(contador_id)
        usuarios[id] = {
            "email": email,
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
        contador_id += 1
        print('Conta criada com sucesso!')
        return usuarios, contador_id, True
    return usuarios, contador_id, False

def fazer_login(usuarios):
    identificador = input('Digite seu email ou CPF:\n').strip()
    senha = input('Digite sua senha:\n').strip()

    usuario = None
    for user in usuarios.values():
        if user['email'] == identificador or user['cpf'] == identificador:
            usuario = user
            break

    if usuario and usuario['senha'] == senha:
        print('Login efetuado com sucesso!')
        return usuario['estado']
    else:
        print('Email/CPF ou senha incorretos!')
        return None

def alterar_senha(usuario):
    nova_senha = input('Digite sua nova senha (mínimo 6 caracteres):\n').strip()
    while len(nova_senha) < 6:
        print('Senha muito curta! Tente novamente.')
        nova_senha = input('Digite sua nova senha (mínimo 6 caracteres):\n').strip()
    usuario['senha'] = nova_senha
    print('Senha alterada com sucesso!')

def excluir_conta(usuario, usuarios):
    for id, user in usuarios.items():
        if user == usuario:
            del usuarios[id]
            break