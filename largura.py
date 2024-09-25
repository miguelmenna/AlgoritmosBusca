from collections import deque

def menu():
    # Função para exibir o menu principal com as opções
    print("1: Iniciar busca em largura")  # Opção para iniciar a busca em largura
    print("2: Sair")  # Opção para encerrar o programa

def busca_em_largura(grafo, inicio, objetivo):
    # Inicializa a fila com o nó de início e o caminho correspondente
    fila = deque([(inicio, [inicio])])
    
    # Conjunto para armazenar nós já visitados, evitando loops
    visitados = set()
    # Lista para registrar todos os nós testados durante a busca
    nos_testados = []

    # Enquanto houver nós na fila para serem explorados
    while fila:
        # Remove o primeiro nó da fila (busca em largura, FIFO)
        no_atual, caminho = fila.popleft()
        # Adiciona o nó atual à lista de nós testados
        nos_testados.append(no_atual)
        
        # Se o nó atual já foi visitado, pula para a próxima iteração
        if no_atual in visitados:
            continue
        
        # Marca o nó como visitado
        visitados.add(no_atual)

        # Verifica se o nó atual é o objetivo
        if no_atual == objetivo:
            # Retorna o caminho encontrado e a lista de nós testados
            return caminho, nos_testados

        # Adiciona todos os vizinhos do nó atual à fila
        for vizinho in grafo[no_atual]:
            # Apenas vizinhos não visitados são considerados
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))

    # Se nenhum caminho foi encontrado, retorna None e os nós testados
    return None, nos_testados  

# Definição do grafo como um dicionário, onde os nós têm listas de vizinhos e os pesos das arestas
grafo = {
    'A': {'C': 1},
    'B': {'C': 1, 'D': 1},
    'C': {'A': 1, 'B': 1, 'G': 1},
    'D': {'B': 1, 'E': 2},
    'E': {'D': 1, 'F': 1},
    'F': {'E': 2, 'J': 1},
    'G': {'C': 1, 'H': 1, 'K': 1},
    'H': {'K': 1, 'G': 1, 'I': 1, 'L': 2},
    'I': {'H': 1, 'J': 1},
    'J': {'F': 1, 'I': 1, 'M': 2},
    'K': {'G': 1, 'N': 2, 'H': 1},
    'L': {'H': 1, 'M': 2},
    'M': {'J': 1, 'P': 2, 'L': 2},
    'N': {'K': 1, 'O': 1, 'Q': 2},
    'O': {'N': 2, 'P': 2},
    'P': {'M': 2, 'O': 1, 'T': 2},
    'Q': {'N': 2, 'R': 1},
    'R': {'Q': 2, 'S': 1},
    'S': {'R': 1, 'T': 2},
    'T': {'P': 2, 'U': 1, 'S': 1},
    'U': {'T': 2}
}

def main():
    # Loop principal do programa, repetindo o menu até o usuário escolher sair
    while True:
        print("\n")
        menu()  # Exibe o menu de opções
        escolha = input("Digite o número da opção desejada: ")  # Recebe a escolha do usuário
        
        if escolha == '1':
            # Solicita o nó de início e o nó de objetivo ao usuário
            inicio = input("Digite o estado inicial: ")
            objetivo = input("Digite o estado final: ")

            # Executa a busca em largura com base nos nós fornecidos
            caminho_encontrado, nos_testados = busca_em_largura(grafo, inicio, objetivo)

            # Se um caminho foi encontrado, exibe o trajeto
            if caminho_encontrado:
                print(f"Caminho encontrado de {inicio} a {objetivo}: {caminho_encontrado}")
            else:
                # Se não for encontrado, informa ao usuário
                print(f"Nenhum caminho encontrado de {inicio} a {objetivo}")
            
            # Exibe a lista de todos os nós que foram testados durante a busca
            print(f"Nós testados: {nos_testados}")
        
        elif escolha == '2':
            # Se o usuário escolher sair, encerra o programa
            print("Saindo do programa...")
            break
        else:
            # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa, chama a função principal
if __name__ == "__main__":
    main()
