from estado import salvar_usuarios, carregar_usuarios
from pensamentos import cadastrar_pensamento, visualizar_pensamento, concluir_pensamento, mostrar_sample_diario
from usuario import criar_conta, fazer_login, alterar_senha, excluir_conta

def menu(estado, usuarios, contador_id, usuario_atual):
    opcao = ''
    while opcao != '0':
        opcao = input(f'Digite: \n1 -> Cadastrar pensamento\n2 -> Visualizar pensamento diário\n3 -> Concluir pensamento\n4 -> Visualizar sample diário\n5 -> Perfil\n0 -> Sair\n').strip()
        if opcao == '1':
            cadastrar_pensamento(estado)
        elif opcao == '2':
            visualizar_pensamento(estado)
        elif opcao == '3':
            concluir_pensamento(estado)
        elif opcao == '4':
            mostrar_sample_diario(estado)
        elif opcao == '5':
            perfil(usuario_atual, usuarios, contador_id)
        elif opcao == '0':
            salvar_usuarios(usuarios, contador_id)
            print('Até amanhã!')
        else:
            print('Opção inválida!')

def perfil(usuario_atual, usuarios, contador_id):
    opcao = ''
    while opcao != '0':
        print(f"Email: {usuario_atual['email']}\nSenha: {usuario_atual['senha']}")
        opcao = input('1 -> Alterar senha\n2 -> Excluir conta\n0 -> Voltar\n').strip()
        if opcao == '1':
            alterar_senha(usuario_atual)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '2':
            excluir_conta(usuario_atual, usuarios)
            salvar_usuarios(usuarios, contador_id)
            print('Conta excluída com sucesso!')
            print('Nunca é um adeus...')
            exit()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

usuarios, contador_id = carregar_usuarios()
estado = None
usuario_atual = None

while estado is None:
    print('1 -> Criar conta\n2 -> Fazer login')
    opcao = input('Escolha uma opção:\n').strip()

    if opcao == '1':
        usuarios, contador_id, sucesso = criar_conta(usuarios, contador_id)
        if sucesso:
            salvar_usuarios(usuarios, contador_id)
    elif opcao == '2':
        if not usuarios:
            print('Nenhum usuário cadastrado. Por favor, crie uma conta primeiro.')
        else:
            estado = fazer_login(usuarios)
            if estado:
                for id, user in usuarios.items():
                    if user['estado'] == estado:
                        usuario_atual = user
                        break
    else:
        print('Opção inválida!')

menu(estado, usuarios, contador_id, usuario_atual)