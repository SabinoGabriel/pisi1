import datetime

def salvar_usuarios(usuarios, contador_id, arquivo='usuarios.txt'):
    with open(arquivo, 'w') as f:
        f.write(f"contador_id:{contador_id}\n")
        for id, dados in usuarios.items():
            f.write(f"---\n")
            f.write(f"{id}:{dados['email']}:{dados['cpf']}:{dados['senha']}\n")
            f.write("estado:\n")
            pensamento_diario = dados['estado']['pensamento_diario']
            f.write(f"pensamento_diario:{pensamento_diario['title'] if pensamento_diario else 'None'}\n")
            f.write(f"descanso:{dados['estado']['descanso']}\n")
            f.write(f"data:{dados['estado']['data']}\n")
            f.write("pensamentos:\n")
            for pensamento in dados['estado']['pensamentos']:
                f.write(f"{pensamento['title']}\n")
            f.write("aux_list:\n")
            for pensamento in dados['estado']['aux_list']:
                f.write(f"{pensamento['title']}\n")
            f.write("sample:\n")
            for pensamento in dados['estado']['sample']:
                f.write(f"{pensamento['title']}\n")

            f.write("mensal:\n")
            for key, value in dados['estado']['mensal'].items():
                f.write(f"{key}:{value}\n")
            f.write("anual:\n")
            for key, value in dados['estado']['anual'].items():
                f.write(f"{key}:{value}\n")

def carregar_usuarios(arquivo='usuarios.txt'):
    usuarios = {}
    contador_id = 0
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            contador_id = int(linhas[0].split(':')[1].strip())
            i = 1
            while i < len(linhas):
                if linhas[i].strip() == '---':
                    i += 1
                    if i >= len(linhas):
                        break
                    partes = linhas[i].strip().split(':')
                    if len(partes) != 4:
                        i += 1
                        continue
                    id, email, cpf, senha = partes
                    i += 2
                    pensamento_diario_str = linhas[i].split(':')[1].strip()
                    pensamento_diario = {'title': pensamento_diario_str} if pensamento_diario_str != 'None' else None
                    i += 1
                    descanso = linhas[i].split(':')[1].strip() == 'True'
                    i += 1
                    data_str = linhas[i].split(':')[1].strip()
                    data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date() if data_str != 'None' else None
                    i += 2
                    pensamentos = []
                    while linhas[i].strip() != 'aux_list:':
                        titulo = linhas[i].strip()
                        if titulo:
                            pensamentos.append({'title': titulo})
                        i += 1
                    i += 1
                    aux_list = []
                    while linhas[i].strip() != 'sample:':
                        titulo = linhas[i].strip()
                        if titulo:
                            aux_list.append({'title': titulo})
                        i += 1
                    i += 1
                    sample = []
                    while i < len(linhas) and not (linhas[i].strip() in ['mensal:', 'anual:', '---']):
                        titulo = linhas[i].strip()
                        if titulo:
                            sample.append({'title': titulo})
                        i += 1

                    mensal = {'Creations': 0, 'Conclusions': 0, 'Views': 0}
                    if i < len(linhas) and linhas[i].strip() == 'mensal:':
                        i += 1
                        while i < len(linhas) and not (linhas[i].strip() in ['anual:', '---']):
                            partes = linhas[i].strip().split(':')
                            if len(partes) == 2:
                                key, value = partes
                                mensal[key] = int(value)
                            i += 1

                    anual = {'Creations': 0, 'Conclusions': 0, 'Views': 0}
                    if i < len(linhas) and linhas[i].strip() == 'anual:':
                        i += 1
                        while i < len(linhas) and not linhas[i].strip() == '---':
                            partes = linhas[i].strip().split(':')
                            if len(partes) == 2:
                                key, value = partes
                                anual[key] = int(value)
                            i += 1

                    estado = {
                        'pensamento_diario': pensamento_diario,
                        'descanso': descanso,
                        'data': data,
                        'pensamentos': pensamentos,
                        'aux_list': aux_list,
                        'sample': sample,
                        'mensal': mensal,
                        'anual': anual
                    }
                    usuarios[id] = {'email': email, 'cpf': cpf, 'senha': senha, 'estado': estado}
                else:
                    i += 1
        print('Bem-vindo!!')
    except FileNotFoundError:
        print('Bem-vindo!')
    return usuarios, contador_id