from estado import salvar_estado, carregar_estado
from pensamentos import cadastrar_pensamento, visualizar_pensamento, concluir_pensamento, mostrar_sample_diario

estado = carregar_estado()

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
            salvar_estado(estado)
            print('Até amanhã!')
        else:
            print('Opção inválida!')

menu(estado)
