class NavigationNode:
    def __init__(self, maxVizinhos=8, vizinhoCount=8, blocked=False, x=0, y=0, GCost=0, HCost=0, FCost=0,
                 pai=[], vizinhos=[]):
        self.maxVizinhos = maxVizinhos
        # Numero de vizinhos que este nó possui
        self.vizinhoCount = vizinhoCount
        # Este nó é um bloqueio ?
        self.blocked = blocked
        # Coordenadas do nó
        self.x = x
        self.y = y
        # Custo da origem ate este nó
        self.GCost = GCost
        # Custo deste nó ate o destino
        self.HCost = HCost
        # Cust total do nó
        self.FCost = FCost
        self.pai = pai
        self.vizinhos = vizinhos

    def adicionaVizinhos(self):
        self.vizinhos.append(NavigationNode())
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    #     self.maxVizinhos = 8
    #     # Numero de vizinhos que este nó possui
    #     self.vizinhoCount = 8
    #     # Este nó é um bloqueio ?
    #     self.blocked = False
    #     # Custo da origem ate este nó
    #     self.GCost = 0
    #     # Custo deste nó ate o destino
    #     self.HCost = 0
    #     # Cust total do nó
    #     self.FCost = 0
    #     self.pai = [NavigationNode]
    #     self.vizinho = [NavigationNode]


class StatusEnum:
    UNPROCCESSED = 1
    FOUND = 2
    IMPOSSIBLE = 3


class Path:
    start = NavigationNode
    end = NavigationNode
    status = StatusEnum()


def calculateHCost(current, goal):
    absX = abs(current.x - goal.x)
    absY = abs(current.y - goal.y)

    if absX > absY:
        h = 14 * absY + 10 * (absX - absY)
    else:
        h = 14 * absX + 10 * (absY - absX)
    return h


def buscaVizinhos(current):
    contador = 0
    # Cima
    if (current[0] != 0 and matriz[current[0] - 1][current[1]] == 0): contador += 1
    # Baixo
    if (current[1] != len(matriz[0]) - 1 and matriz[current[0] + 1][current[1]] == 0): contador += 1
    # Esquerda
    if (current[1] != 0 and matriz[current[0]][current[1] - 1] == 0): contador += 1
    # Direita
    if (current[1] != len(matriz[0]) - 1 and matriz[current[0]][current[1] + 1] == 0): contador += 1
    # Cima Direita
    if (current[0] != 0 and current[1] != len(matriz[0]) - 1 and matriz[current[0] - 1][
        current[1] + 1] == 0): contador += 1
    # Cima Esquerda
    if (current[0] != 0 and current[1] != 0 and matriz[current[0] - 1][current[1] - 1] == 0): contador += 1
    # Baixo Direita
    if (current[0] != len(matriz) - 1 and current[1] != len(matriz[0]) - 1 and matriz[current[0] + 1][
        current[1] + 1] == 0): contador += 1
    # Baixo Esquerda
    if (current[0] != len(matriz) - 1 and current[1] != 0 and matriz[current[0] + 1][
        current[1] - 1] == 0): contador += 1

    return contador


class PathFinder:
    def FindPath(self, start=NavigationNode(), end=NavigationNode()):
        openList = []
        closedList = []

        path = Path()
        path.start = start
        path.end = end
        path.status = path.status.UNPROCCESSED

        # Inicializa o nó inicial
        start.GCost = 0
        start.HCost = calculateHCost(start, end)
        start.FCost = start.GCost + start.HCost
        end.pai = start.pai = []
        start.maxVizinhos = 8
        start.vizinhoCount = buscaVizinhos([start.x, start.y])
        start = NavigationNode()

        openList.append(start)

        while path.status == StatusEnum.UNPROCCESSED:

            # Se a lista ABERTA estiver vazia, não pudemos encontrar um caminho.
            if len(openList) == 0:
                path.status = StatusEnum.IMPOSSIBLE
                break
            # Ordena a lista aberta pelo menor
            openList.sort(key=lambda x: (x.HCost + x.GCost))
            # Pega o nó com menor FCost da lista ABERTA
            current = openList[0]
            # Remove o no atual da lista ABERTA
            openList.remove(openList[0])

            # Adiciona na lista FECHADA
            closedList.append(current)

            # Se este for o nó destino, terminamos
            if current == end:
                path.status = StatusEnum.FOUND
                break

            blockedNode = object
            blockedNodeCount = 0

            # Processa os nós filhos do nó atual
            for vizinhoIndex in range(current.vizinhoCount):
                vizinho = current.vizinhos[vizinhoIndex]

                # Ignora se este vizinho for um bloqueio
                if vizinho.blocked:
                    blockedNode[blockedNodeCount + 1] = vizinho
                    continue

                # Ignora se este vizinho estiver na lista fechada
                if vizinho in closedList:
                    continue

                # Custo de movimento Ortogonal: 10; Diagonal: 14

                movementCost = 10
                if vizinho.x != current.x and vizinho.y != current.y:
                    movementCost = 14

                ignoreNode = False
                for i in range(blockedNodeCount):
                    blocked = blockedNode[i]
                    # Current na mesma linha do bloqueio
                    if current.x == blocked.x:
                        if vizinho.x != blocked.x and vizinho.y == blocked.y:
                            ignoreNode = True
                            break
                    # Current na mesma coluna do bloqueio
                    elif current.y == blocked.y:
                        if vizinho.y != blocked.y and vizinho.x == blocked.x:
                            ignoreNode = True
                            break

                if ignoreNode:
                    continue

                if vizinho in openList:
                    # Este nó já está na lista aberta, podemos melhorar o caminho até ele?
                    betterGCost = current.GCost + movementCost
                    if betterGCost < vizinho.GCost:
                        vizinho.parent = current
                        vizinho.GCost = betterGCost
                        vizinho.FCost = vizinho.GCost + vizinho.HCost
                else:
                    vizinho.parent = current
                    vizinho.GCost = current.GCost + movementCost
                    vizinho.HCost = calculateHCost(vizinho, end)
                    vizinho.FCost = vizinho.GCost + vizinho.HCost
                    openList.append(vizinho)

        return path


matriz = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

resultado = PathFinder.FindPath(NavigationNode(x=0, y=0), NavigationNode(x=4, y=5))
print(resultado)
