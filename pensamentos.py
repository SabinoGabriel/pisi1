import datetime
import random

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
        print(f'Pensamento do dia:\n {estado["pensamento_diario"]["title"]}')
    return

def concluir_pensamento(estado):
    if len(estado['pensamentos']) == 0:
        print('Nenhum pensamento cadastrado!')

    elif estado['data'] != datetime.date.today():
        print('Pensamento do dia ainda não visualizado!')

    elif estado['descanso']:
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')

    elif estado['pensamento_diario'] is not None:
        print(f'Pensamento do dia:\n {estado["pensamento_diario"]["title"]}')
        
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

        if opcao == '1' and not estado['descanso']:
            print('Selecione o pensamento que deseja editar:')
            print(f'0 -> {estado["pensamento_diario"]["title"]}')
            for i in range(len(estado['sample'])):
                print(f'{i+1} -> {estado["sample"][i]["title"]}')
            
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

        elif opcao == '1' and estado['descanso']:
            print('Selecione o pensamento que deseja editar:')
            for i in range(len(estado['sample'])):
                print(f'{i} -> {estado['sample'][i]["title"]}')
            
            escolha = int(input('Digite o número do pensamento que deseja editar:\n'))
            if 0 >= escolha <= len(estado['sample']):
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
            else:
                print('Escolha inválida.')
       
        elif opcao != '2':
            print('Opção inválida!')

    return