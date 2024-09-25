def menu():
    # Função para exibir o menu principal com as opções
    print("1: Começar")  # Opção para iniciar a busca gulosa
    print("2: Sair")    # Opção para sair do programa

def busca_guloso(grafo, inicio, fim):
    # Inicializa uma fila com o nó de início e o caminho vazio
    fila = [(inicio, [])]
    # Conjunto para rastrear os nós visitados
    visitados = set()

    # Enquanto houver nós na fila
    while fila:
        # Remove o primeiro elemento da fila (busca gulosa, por proximidade)
        nodo_atual, caminho = fila.pop(0)

        # Se o nó atual já foi visitado, ignora e passa para o próximo
        if nodo_atual in visitados:
            continue

        # Atualiza o caminho com o nó atual
        caminho = caminho + [nodo_atual]
        # Marca o nó atual como visitado
        visitados.add(nodo_atual)

        # Se o nó atual é o destino, retorna o caminho e os nós visitados
        if nodo_atual == fim:
            return caminho, visitados

        # Ordena os vizinhos pelo valor da aresta (menor custo) e os adiciona à fila
        for vizinho in sorted(grafo[nodo_atual], key=lambda k: grafo[nodo_atual][k]):
            if vizinho not in visitados:
                fila.append((vizinho, caminho))

    # Se nenhum caminho for encontrado, retorna None
    return None, None

def main():
    # Definição do grafo como um dicionário, onde as chaves são nós e os valores são dicionários com os vizinhos e seus respectivos custos
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

    # Loop principal do programa, repetindo o menu até o usuário escolher sair
    while True:
        print("\n")
        menu()  # Exibe o menu de opções
        escolha = input("Digite sua escolha: ")  # Recebe a escolha do usuário

        if escolha == '2':
            # Se a escolha for '2', o programa é encerrado
            print("Saindo do programa...")
            break
        elif escolha == '1':
            # Se a escolha for '1', solicita o nó de início e o nó de fim ao usuário
            inicio = input("Digite o estado inicial: ")
            fim = input("Digite o estado final: ")

            # Executa a busca gulosa e obtém o caminho e os nós visitados
            caminho, visitados = busca_guloso(grafo, inicio, fim)
            print(f"Caminho encontrado entre {inicio} e {fim} com Guloso é:", caminho)
            print("Nós visitados:", visitados)
        else:
            # Se a escolha for inválida, exibe uma mensagem de erro
            print("Escolha inválida!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
