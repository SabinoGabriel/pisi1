import datetime

def salvar_usuarios(usuarios, arquivo='usuarios.txt'):
    with open(arquivo, 'w') as f:
        for email, dados in usuarios.items():
            f.write(f"{email}:{dados['cpf']}:{dados['senha']}\n")
            f.write("estado:\n")
            f.write(f"pensamento_diario:{dados['estado']['pensamento_diario']}\n")
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
            f.write("---\n")
    print('Usuários e estados salvos com sucesso!')

def carregar_usuarios(arquivo='usuarios.txt'):
    usuarios = {}
    try:
        with open(arquivo, 'r') as f:
            linhas = f.read().split('---')
            for bloco in linhas:
                linhas_bloco = bloco.strip().split('\n')
                if len(linhas_bloco) < 4:
                    continue
                email, cpf, senha = linhas_bloco[0].split(':')
                estado = {
                    'pensamento_diario': linhas_bloco[2].split(':')[1].strip(),
                    'descanso': linhas_bloco[3].split(':')[1].strip() == 'True',
                    'data': datetime.datetime.strptime(linhas_bloco[4].split(':')[1].strip(), '%Y-%m-%d').date() if linhas_bloco[4].split(':')[1].strip() else None,
                    'pensamentos': [{'title': linha.strip()} for linha in linhas_bloco[6:linhas_bloco.index('aux_list:')]],
                    'aux_list': [{'title': linha.strip()} for linha in linhas_bloco[linhas_bloco.index('aux_list:')+1:linhas_bloco.index('sample:')]],
                    'sample': [{'title': linha.strip()} for linha in linhas_bloco[linhas_bloco.index('sample:')+1:]]
                }
                usuarios[email] = {'cpf': cpf, 'senha': senha, 'estado': estado}
        print('Usuários carregados com sucesso!')
    except FileNotFoundError:
        print('Nenhum usuário cadastrado ainda.')
    return usuarios
