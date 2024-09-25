import heapq

def menu():
    # Função para exibir o menu principal com as opções
    print("1: Começar")  # Opção para iniciar a busca A*
    print("2: Sair")     # Opção para sair do programa

def a_estrela(grafo, inicio, fim, heuristica):
    # Inicializa a fila de prioridades (heap) com o nó inicial, custo 0 e caminho vazio
    fila = [(0, inicio, [])]
    # Dicionário que mantém o custo acumulado para chegar a cada nó
    custos = {inicio: 0}
    # Conjunto para armazenar os nós visitados
    visitados = set()

    # Enquanto houver nós na fila de prioridades
    while fila:
        # Remove o nó com menor custo da fila de prioridades
        _, nodo_atual, caminho = heapq.heappop(fila)

        # Se o nó já foi visitado, pula para o próximo
        if nodo_atual in visitados:
            continue

        # Atualiza o caminho com o nó atual
        caminho = caminho + [nodo_atual]
        # Marca o nó atual como visitado
        visitados.add(nodo_atual)

        # Se o nó atual é o objetivo, retorna o caminho e os nós visitados
        if nodo_atual == fim:
            return caminho, visitados

        # Para cada vizinho do nó atual
        for vizinho, peso in grafo[nodo_atual].items():
            # Calcula o custo g (do início até o vizinho)
            custo_g = custos[nodo_atual] + peso
            # Calcula o custo f (custo g + valor da heurística para o vizinho)
            custo_f = custo_g + heuristica[vizinho]

            # Se o vizinho ainda não foi visitado ou o custo g encontrado é menor que o atual
            if vizinho not in custos or custo_g < custos[vizinho]:
                # Atualiza o custo acumulado para o vizinho
                custos[vizinho] = custo_g
                # Adiciona o vizinho à fila de prioridades com o custo f
                heapq.heappush(fila, (custo_f, vizinho, caminho))

    # Se nenhum caminho for encontrado, retorna None
    return None, None

def main():
    # Definição do grafo, onde cada nó tem seus vizinhos e o custo de transição entre eles
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

    # Heurística de estimativas de custo direto para o objetivo
    heuristica = {
        'A': 7,
        'B': 6,
        'C': 5,
        'D': 4,
        'E': 3,
        'F': 2,
        'G': 6,
        'H': 5,
        'I': 3,
        'J': 2,
        'K': 4,
        'L': 2,
        'M': 1,
        'N': 3,
        'O': 2,
        'P': 1,
        'Q': 3,
        'R': 2,
        'S': 1,
        'T': 0,  # O objetivo final (T) tem heurística 0
        'U': 1
    }

    # Loop principal para interagir com o usuário
    while True:
        menu()  # Exibe o menu
        escolha = input("Digite sua escolha: ")  # Pede a escolha do usuário

        if escolha == '2':
            # Se o usuário escolher "2", o programa encerra
            print("Saindo do programa...")
            break
        elif escolha == '1':
            # Se o usuário escolher "1", pede o nó de início e o nó de destino
            inicio = input("Digite o estado inicial: ")
            fim = input("Digite o estado final: ")

            # Realiza a busca A* com o grafo, nó inicial, final e heurística
            caminho, visitados = a_estrela(grafo, inicio, fim, heuristica)
            # Exibe o caminho encontrado e os nós visitados
            print(f"Caminho mais curto com A* de {inicio} a {fim} é: ", caminho)
            print("Nós visitados:", visitados)
        else:
            # Se o usuário fizer uma escolha inválida, exibe uma mensagem de erro
            print("Escolha inválida!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
