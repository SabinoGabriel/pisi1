from estado import salvar_usuarios, carregar_usuarios
from pensamentos import cadastrar_pensamento, visualizar_pensamento, concluir_pensamento, mostrar_sample_diario
from usuario import criar_conta, fazer_login

usuarios = carregar_usuarios()
estado = None

while estado is None:
    print('1 -> Criar conta\n2 -> Fazer login')
    opcao = input('Escolha uma opção:\n').strip()

    if opcao == '1':
        usuarios = criar_conta(usuarios)
        salvar_usuarios(usuarios)
    elif opcao == '2':
        if not usuarios:
            print('Nenhum usuário cadastrado. Por favor, crie uma conta primeiro.')
        else:
            estado = fazer_login(usuarios)
    else:
        print('Opção inválida!')

def menu(estado):
    opcao = ''
    while opcao != '0':
        opcao = input(f'Digite: \n1 -> Cadastrar pensamento\n2 -> Visualizar pensamento diário\n3 -> Concluir pensamento\n4 -> Visualizar sample diário\n0 -> Sair\n').strip()
        if opcao == '1':
            cadastrar_pensamento(estado)
        elif opcao == '2':
            visualizar_pensamento(estado)
        elif opcao == '3':
            concluir_pensamento(estado)
        elif opcao == '4':
            mostrar_sample_diario(estado)
        elif opcao == '0':
            salvar_usuarios(usuarios)
            print('Até amanhã!')
        else:
            print('Opção inválida!')

menu(estado)