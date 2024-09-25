def exibir_menu():
    # Função para mostrar as opções disponíveis no menu
    print("1: Iniciar")  # Opção para iniciar a busca
    print("2: Encerrar")  # Opção para sair do programa

def busca_profundidade(grafo, origem, destino):
    # Inicializa a pilha com o nó de origem e o caminho correspondente
    caminho_atual = [(origem, [origem])]
    # Conjunto para armazenar nós que já foram visitados
    visitados = set()
    # Lista para guardar todos os caminhos tentados durante a busca
    tentativas_caminhos = []

    # Enquanto ainda houver nós para explorar na pilha
    while caminho_atual:
        # Retira o último nó e caminho da pilha (busca em profundidade)
        (vertice, trajeto) = caminho_atual.pop()
        # Adiciona o caminho atual na lista de tentativas
        tentativas_caminhos.append(trajeto)

        # Se o nó ainda não foi visitado
        if vertice not in visitados:
            # Verifica se o nó atual é o destino
            if vertice == destino:
                # Exibe todos os caminhos que foram tentados
                print("\nCaminhos tentados durante a busca:")
                for tentativa in tentativas_caminhos:
                    print(tentativa)
                # Retorna o caminho que levou até o destino
                return trajeto

            # Marca o nó como visitado
            visitados.add(vertice)
            # Adiciona todos os vizinhos do nó atual na pilha
            for vizinho in grafo[vertice]:
                caminho_atual.append((vizinho, trajeto + [vizinho]))

    # Se nenhum caminho foi encontrado, retorna None
    return None

# Definição do grafo como um dicionário, onde cada nó tem uma lista de vizinhos e pesos
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

def iniciar_programa():
    # Loop principal do programa, exibindo o menu até o usuário decidir sair
    while True:
        print("\n")
        exibir_menu()  # Exibe o menu de opções
        opcao = input("Escolha a opção desejada: ")  # Recebe a escolha do usuário

        if opcao == '1':
            # Solicita o ponto de partida e de destino ao usuário
            origem = input("Informe o ponto de partida: ")
            destino = input("Informe o ponto de chegada: ")

            # Chama a função de busca em profundidade
            caminho = busca_profundidade(grafo, origem, destino)

            # Se um caminho foi encontrado, exibe o trajeto
            if caminho:
                print(f"\nCaminho encontrado de {origem} até {destino}: {caminho}")
            else:
                # Caso contrário, informa que nenhum caminho foi encontrado
                print(f"\nNenhum caminho encontrado de {origem} até {destino}")
        elif opcao == '2':
            # Opção para encerrar o programa
            print("Encerrando o programa...")
            break
        else:
            # Trata a entrada de uma opção inválida
            print("Opção inválida, por favor tente novamente.")

# Ponto de entrada do programa, executa a função principal
if __name__ == "__main__":
    iniciar_programa()
