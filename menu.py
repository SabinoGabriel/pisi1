from estado import salvar_usuarios, carregar_usuarios
from pensamentos import cadastrar_pensamento, visualizar_pensamento, concluir_pensamento, mostrar_sample_diario
from usuario import criar_conta, fazer_login, alterar_senha, excluir_conta

def limpar_tela():
    print("\033[2J\033[H", end="")

def menu(estado, usuarios, contador_id, usuario_atual):
    limpar_tela()
    opcao = ''
    while opcao != '0':
        print("=" * 30)
        print("MENU PRINCIPAL")
        print("=" * 30)
        print('1 -> Cadastrar pensamento')
        print('2 -> Visualizar pensamento diário')
        print('3 -> Concluir pensamento')
        print('4 -> Visualizar sample diário')
        print('5 -> Perfil')
        print('0 -> Sair')
        opcao = input('Digite a opção desejada:\n').strip()
        limpar_tela()

        if opcao == '1':
            limpar_tela()
            cadastrar_pensamento(estado)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '2':
            limpar_tela()
            visualizar_pensamento(estado)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '3':
            limpar_tela()
            concluir_pensamento(estado)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '4':
            limpar_tela()
            mostrar_sample_diario(estado)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '5':
            limpar_tela()
            if usuario_atual:
                perfil(usuario_atual, usuarios, contador_id)
            else:
                print("Nenhum usuário logado.")
        elif opcao == '0':
            salvar_usuarios(usuarios, contador_id)
            print('Até amanhã!')
        else:
            print('Opção inválida!')
        input("Pressione Enter para continuar...")
        limpar_tela()

def perfil(usuario_atual, usuarios, contador_id):
    limpar_tela()
    opcao = ''
    while opcao != '0':
        print("=" * 30)
        print("PERFIL")
        print("=" * 30)
        print(f"Email: {usuario_atual['email']}")
        print(f"Senha: {usuario_atual['senha']}")
        print('1 -> Alterar senha')
        print('2 -> Excluir conta')
        print('0 -> Voltar')
        opcao = input('Digite a opção desejada:\n').strip()

        if opcao == '1':
            limpar_tela()
            alterar_senha(usuario_atual)
            salvar_usuarios(usuarios, contador_id)
        elif opcao == '2':
            limpar_tela()
            excluir_conta(usuario_atual, usuarios)
            salvar_usuarios(usuarios, contador_id)
            print('Conta excluída com sucesso!')
            print('Nunca é um adeus...')
            exit()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')
        input("Pressione Enter para continuar...")
        limpar_tela()

limpar_tela()
usuarios, contador_id = carregar_usuarios()
estado = None
usuario_atual = None
opcao = ''

while estado is None and opcao != '0':
    print("=" * 30)
    print("INÍCIO")
    print("=" * 30)
    print('1 -> Criar conta')
    print('2 -> Fazer login')
    print('0 -> Encerrar')
    opcao = input('Escolha uma opção:\n').strip()
    limpar_tela()

    if opcao == '1':
        limpar_tela()
        usuarios, contador_id, sucesso = criar_conta(usuarios, contador_id)
        if sucesso:
            salvar_usuarios(usuarios, contador_id)
    elif opcao == '2':
        limpar_tela()
        if not usuarios:
            print('Nenhum usuário cadastrado. Por favor, crie uma conta primeiro.')
        else:
            usuario_id = fazer_login(usuarios)
            if usuario_id:
                usuario_atual = usuarios[usuario_id]
                estado = usuario_atual['estado']
                menu(estado, usuarios, contador_id, usuario_atual)
                opcao = ''
                estado = None
                usuario_atual = None
                usuario_id = None
    elif opcao == '0':
        print('Até mais!')
    else:
        print('Opção inválida!')
    input("Pressione Enter para continuar...")
    limpar_tela()
