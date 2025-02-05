import random
import datetime


def salvar_estado(estado, arquivo='estado.txt'):
    with open(arquivo, 'w') as f:
        f.write(f"pensamento_diario:{estado['pensamento_diario']['title'] if estado['pensamento_diario'] else ''}\n")
        f.write(f"descanso:{estado['descanso']}\n")
        f.write(f"data:{estado['data']}\n")
        f.write("pensamentos:\n")
        for pensamento in estado['pensamentos']:
            f.write(f"{pensamento['title']}\n")
        f.write("aux_list:\n")
        for pensamento in estado['aux_list']:
            f.write(f"{pensamento['title']}\n")
        f.write("sample:\n")
        for pensamento in estado['sample']:
            f.write(f"{pensamento['title']}\n")
    print('Estado salvo com sucesso!')

def carregar_estado(arquivo='estado.txt'):
    estado = {
        'pensamentos': [],
        'pensamento_diario': None,
        'descanso': False,
        'data': None,
        'aux_list': [],
        'sample': [],
    }
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            estado['pensamento_diario'] = {'title': linhas[0].split(':')[1].strip()} if linhas[0].split(':')[1].strip() else None
            estado['descanso'] = linhas[1].split(':')[1].strip() == 'True'
            estado['data'] = datetime.datetime.strptime(linhas[2].split(':')[1].strip(), '%Y-%m-%d').date() if linhas[2].split(':')[1].strip() else None

            secao = None
            for linha in linhas[3:]:
                linha = linha.strip()
                if not linha:
                    continue
                if linha.endswith(':'):
                    secao = linha[:-1]
                elif secao == 'pensamentos':
                    estado['pensamentos'].append({'title': linha})
                elif secao == 'aux_list':
                    estado['aux_list'].append({'title': linha})
                elif secao == 'sample':
                    estado['sample'].append({'title': linha})
        print('Estado carregado com sucesso!')
    except FileNotFoundError:
        print('Seja bem-vindo! Vamos começar a cadastrar seus pensamentos!')
    return estado

def cadastrar_pensamento(estado):
    if len(estado['pensamentos']) == 20:
        print('Limite de pensamentos atingido!')
        return
    
    titulo = input('Digite o título do pensamento:\n').capitalize().strip()

    for pensamento in estado['pensamentos']:
        if pensamento['title'] == titulo:
            print('Pensamento já cadastrado!')
            return
    
    pensamento = {'title': titulo}
    estado['pensamentos'].append(pensamento)
    estado['aux_list'].append(pensamento)
    print('Pensamento cadastrado com sucesso!')
    return

def visualizar_pensamento(estado):

    if len(estado['pensamentos']) == 0:
        print('Nenhum pensamento cadastrado!')
        return

    elif estado['descanso'] == True and estado['data'] == datetime.date.today():
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')

    elif estado['data'] != datetime.date.today():
        estado['descanso'] = False
        estado['data'] = datetime.date.today()

        if len(estado['aux_list']) == 0:
            print("Você visualizou todos os pensamentos que foram cadastrados nos últimos dias, agora reiniciaremos!")
            estado['aux_list'] = estado['pensamentos'].copy()

        estado['pensamento_diario'] = estado['aux_list'][random.randint(0,len(estado['aux_list'])-1)]
        estado['aux_list'].remove(estado['pensamento_diario'])
        print(f'Pensamento do dia:\n{estado["pensamento_diario"]["title"]}')


        if len(estado['pensamentos']) < 9:
            sample_size = len(estado['pensamentos'])//2
        else:
            sample_size = 4

        daily_index = -1
        for i, pensamento in enumerate(estado['pensamentos']):
            if pensamento == estado['pensamento_diario']:
                daily_index = i
                break
        index_list = list(range(len(estado['pensamentos'])))
        index_list.remove(daily_index)

        estado['sample'].clear()

        index_sample = random.sample(index_list, sample_size)
        for i in range(sample_size):
            estado['sample'].append(estado['pensamentos'][index_sample[i]])

    elif estado['data'] == datetime.date.today():
        print(f'Pensamento do dia:\n {estado['pensamento_diario']['title']}')
    return

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

def mostrar_sample_diario(estado):
    def obter_titulo_unico():
        repetion = False
        while not repetion:
            novo_titulo = input('Digite o novo título do pensamento:\n').capitalize().strip()
            
            for pensamento in estado['pensamentos']:
                if pensamento['title'] == novo_titulo:
                    print('Esse título já foi cadastrado! Tente outro.')
                    break

            else:
                repetion = True
        return novo_titulo
    if estado['data'] != datetime.date.today():
        print('Você ainda não visualizou o pensamento diário de hoje! Faça isso para poder visualizar o sample de hoje.')
        return
    
    if not estado['sample']:
        print('Você iniciou seu dia com menos de 2 pensamentos cadastrados, logo você não pode obter um sample hoje.')
        return

    opcao = ''
    while opcao != '2':
        if not estado['descanso']:
            print(f'Pensamento diário:\n{estado["pensamento_diario"]["title"]}') 
            print('Sample diário:')
            for pensamento in estado['sample']:
                print(f"- {pensamento['title']}")
        else:
            print('Sample diário:')
            for pensamento in estado['sample']:
                print(f"- {pensamento['title']}")
                
        opcao = input('Você gostaria de editar o título de algum desses pensamentos?\n1 -> Sim\n2 -> Não\n').strip()

        if opcao == '1':
            print('Selecione o pensamento que deseja editar:')
            print(f'0 -> {estado["pensamento_diario"]["title"]}')
            for i in range(len(estado['sample'])):
                print(f'{i+1} -> {estado['sample'][i]["title"]}')
            
            try:
                escolha = int(input('Digite o número do pensamento que deseja editar:\n')) - 1
                if 0 <= escolha < len(estado['sample']):
                    novo_titulo = obter_titulo_unico()

                    if estado['sample'][escolha]['title'] in estado['aux_list']:
                        for pensamento in estado['aux_list']:
                            if pensamento['title'] == estado['sample'][escolha]['title']:
                                pensamento['title'] = novo_titulo
                                break

                    estado['sample'][escolha]['title'] = novo_titulo

                    for pensamento in estado['pensamentos']:
                        if pensamento['title'] == estado['sample'][escolha]['title']:
                            pensamento['title'] = novo_titulo
                            break
                    print('Título do pensamento atualizado com sucesso!')
                elif escolha == -1:
                    novo_titulo = obter_titulo_unico()
                    estado['pensamento_diario']['title'] = novo_titulo

                    for pensamento in estado['pensamentos']:
                        if pensamento['title'] == estado['pensamento_diario']['title']:
                            pensamento['title'] = novo_titulo
                            break
                    print('Título do pensamento atualizado com sucesso!')

                else:
                    print('Escolha inválida.')
            except ValueError:
                print('Escolha inválida.')
        elif opcao != '2':
            print('Opção inválida!')

    return
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
