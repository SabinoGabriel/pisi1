
import random 
import datetime 

problemas = []
problema_diario = None
descanso = False

def cadastrar_problema():
    global problemas
    problema = input('Digite o título do problema:\n')
    problemas.append(problema)
    print('Problema cadastrado com sucesso!')
    return

def visualizar_problema():
    global problemas, problema_diario, descanso
    if len(problemas) == 0:
        print('Nenhum problema cadastrado!')
    elif descanso == True:
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')
    else:
        problema_diario = problemas[-1]
        print(f'Problema do dia:\n {problema_diario}')
    return

def concluir_problema():
    global problemas, problema_diario, descanso
    if len(problemas) == 0:
        print('Nenhum problema cadastrado!')
    elif descanso == True:
        print('Dever cumprido!\nUtilize o resto do dia para descansar.')
    elif problema_diario != None:
        print(f'Problema do dia:\n {problema_diario}')
        problemas.pop()
        print('Problema concluído!\nDescanse sua mente para o próximo desafio.')
        descanso = True
        problema_diario = None
    else:
        print('Você não visualizou o problema do dia!')

    return

def menu():
    opcao = input(f'Digite: \n1 -> Cadastrar problema\n2 -> Visualizar problema\n3 -> Concluir problema\n4 -> Sair\n')

    while True:
        if opcao == '1':
            cadastrar_problema()
        elif opcao == '2':
            visualizar_problema()
        elif opcao == '3':
            concluir_problema()
        elif opcao == '4':
            print('Até amanhã!')
            break
        else:
            print('Opção inválida!')
        opcao = input(f'Digite: \n1 -> Cadastrar problema\n2 -> Visualizar problema\n3 -> Concluir problema\n4 -> Sair\n')

menu()
