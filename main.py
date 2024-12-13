import random
import datetime

estado = {
    'pensamentos': [],
    'pensamento_diario': None,
    'descanso': False,
    'data': None 
}

def cadastrar_pensamento(estado):
    if len(estado['pensamentos']) == 20:
        print('Limite de pensamentos atingido!')
        return
    
    titulo = input('Digite o título do pensamento:\n')
    
    for pensamento in estado['pensamentos']:
        if pensamento['title'] == titulo:
            print('Pensamento já cadastrado!')
            return
    
    pensamento = {'title': titulo}
    estado['pensamentos'].append(pensamento)
    print('Pensamento cadastrado com sucesso!')
    return

def visualizar_pensamento(estado):
    if len(estado['pensamentos']) == 0:
        print('Nenhum pensamento cadastrado!')

    elif estado['descanso'] == True and estado['data'] == datetime.date.today():
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')

    elif estado['data'] != datetime.date.today():
        estado['descanso'] = False
        estado['data'] = datetime.date.today()
        estado['pensamento_diario'] = estado['pensamentos'][random.randint(0,len(estado['pensamentos'])-1)]
        print(f'Pensamento do dia:\n {estado['pensamento_diario']['title']}')

    elif estado['data'] == datetime.date.today():
        print(f'Pensamento do dia:\n {estado['pensamento_diario']}')
    return

# contador = 1
# def visualizar_pensamento_manual(estado):
#     global contador
#     if estado['data'] is None:
#         estado['data'] = datetime.date.today()
#     else:
#         estado['data'] += datetime.timedelta(days=contador)
#         contador += 1
#     if len(estado['pensamentos']) == 0:
#         print('Nenhum pensamento cadastrado!')

#     elif estado['descanso'] == True and estado['data'] == None:
#         print('Dever cumprido!\nUtilize o resto do dia para descansar.')

#     elif estado['data'] != datetime.date.today():
#         estado['descanso'] = False
#         estado['data'] = datetime.date.today()
#         estado['pensamento_diario'] = estado['pensamentos'][random.randint(0,len(estado['pensamentos'])-1)]
#         print(f'Pensamento do dia:\n {estado['pensamento_diario']['title']}')

#     elif estado['data'] == datetime.date.today():
#         print(f'Pensamento do dia:\n {estado['pensamento_diario']}')
#     return

def concluir_pensamento(estado):
    if len(estado['pensamentos']) == 0:
        print('Nenhum pensamento cadastrado!')

    elif estado['data'] != datetime.date.today():
        print('Pensamento do dia ainda não visualizado!')

    elif estado['descanso']:
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')

    elif estado['pensamento_diario'] is not None:
        print(f'Pensamento do dia:\n {estado['pensamento_diario']['title']}')
        
        for pensamento in estado['pensamentos']:
            if pensamento['title'] == estado['pensamento_diario']['title']:
                estado['pensamentos'].remove(pensamento)
                break
        
        print('Pensamento concluído!\nDescanse sua mente para o próximo desafio.')
        estado['descanso'] = True
        estado['pensamento_diario'] = None

    else:
        print('Você não visualizou o pensamento do dia!')

    return

def menu(estado):
    opcao = ''
    while opcao != '4':
        opcao = input(f'Digite: \n1 -> Cadastrar pensamento\n2 -> Visualizar pensamento\n3 -> Concluir pensamento\n4 -> Sair\n')
        if opcao == '1':
            cadastrar_pensamento(estado)
        elif opcao == '2':
            visualizar_pensamento(estado)
        elif opcao == '3':
            concluir_pensamento(estado)
        elif opcao == '4':
            print('Até amanhã!')
        
        # Função para alterar a data manualmente
        # elif opcao == '!':
        #     visualizar_pensamento_manual(estado)
        else:
            print('Opção inválida!')

menu(estado)
