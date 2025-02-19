---

# Pisi1

Este repositório contém um programa para gerenciar pensamentos diários, desenvolvido para a cadeira de Projetos Interdisciplinares 1 do curso de Sistema de Informação.

## Arquivos

- `pensamentos.py`: Contém funções para cadastrar, visualizar, concluir e mostrar um sample diário de pensamentos.
- `menu.py`: Contém o menu principal do programa que permite a interação com o usuário através de opções.
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

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SabinoGabriel/pisi1.git
   cd pisi1
   ```

2. Execute o programa:
   ```bash
   python3 menu.py
   ```

## Estrutura do Estado

O estado do programa é salvo em um arquivo `estado.txt` e contém as seguintes informações:
- `pensamento_diario`: O pensamento diário atual.
- `descanso`: Indica se o pensamento diário foi concluído.
- `data`: A última data em que o pensamento diário foi visualizado.
- `pensamentos`: Lista de todos os pensamentos cadastrados.
- `aux_list`: Lista auxiliar de pensamentos para visualização do pensamento diário.
- `sample`: Sample diário de pensamentos.

---
