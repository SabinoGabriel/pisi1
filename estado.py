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
