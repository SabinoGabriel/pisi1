---

# Projetos Interdisciplinares para Sistemas de Informação 1

Este repositório contém um programa para gerenciar pensamentos diários, desenvolvido para a cadeira de Projetos Interdisciplinares 1 do curso de Bacharelado em Sistemas de Informação da UFRPE.

## Bibliotecas Utilizadas

- `datetime`: Utilizada para manipulação e formatação de datas, essencial para verificar a constância de acesso e gerar retrospectivas mensais e anuais.
- `random`: Utilizada para selecionar pensamentos aleatórios para exibição diária e para o sample diário.

## Organização dos Módulos

- `pensamentos.py`: Contém funções para cadastrar, visualizar, concluir e mostrar um sample diário de pensamentos.
- `menu.py`: Contém o menu principal do programa que permite a interação com o usuário através de opções.
- `usuario.py`: Contém funções para criar conta, fazer login, alterar senha e excluir conta.
- `estado.py`: Contém funções para salvar e carregar o estado do programa em um arquivo.

## Funcionalidades

1. **Cadastrar Pensamento**
   - Adiciona um novo pensamento ao estado atual, garantindo que o título não seja duplicado.

2. **Visualizar Pensamento Diário**
   - Exibe um pensamento diário aleatório e um sample de outros pensamentos cadastrados.

3. **Concluir Pensamento**
   - Marca o pensamento diário como concluído e o remove da lista de pensamentos.

4. **Mostrar Sample Diário**
   - Exibe e permite a edição de um sample diário de pensamentos cadastrados.

5. **Gerenciar Usuário**
   - Criar conta, fazer login, alterar senha e excluir conta.

6. **Verificação de Constância de Acesso**
   - Verifica a constância de acesso dos usuários, incentivando a regularidade no uso do sistema.

7. **Retrospecto Mensal e Anual**
   - Exibe um retrospecto mensal e anual das atividades do usuário, incluindo o número de pensamentos cadastrados, concluídos e visualizados.

## Inovação do Projeto

- **Gamificação**: O sistema inclui uma funcionalidade de gamificação que verifica a constância de acesso dos usuários e gera um retrospecto mensal e anual. Isso incentiva os usuários a manterem uma rotina regular de reflexão e conclusão de pensamentos, promovendo uma melhor organização mental e pessoal.

## Como Executar

1. Abra o terminal e clone o repositório:
   ```sh
   git clone https://github.com/SabinoGabriel/pisi1.git
   cd pisi1
   ```

2. Execute o programa:
   ```sh
   python3 menu.py
   ```

## Estrutura do Estado

O estado do programa é salvo em um arquivo `usuarios.txt` e contém as seguintes informações:
- `pensamento_diario`: O pensamento diário atual.
- `descanso`: Indica se o pensamento diário foi concluído.
- `data`: A última data em que o pensamento diário foi visualizado.
- `pensamentos`: Lista de todos os pensamentos cadastrados.
- `aux_list`: Lista auxiliar de pensamentos para visualização do pensamento diário.
- `sample`: Sample diário de pensamentos.
- `mensal`: Retrospecto mensal das atividades (criações, conclusões, visualizações).
- `anual`: Retrospecto anual das atividades (criações, conclusões, visualizações).

---
