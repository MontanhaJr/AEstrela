def heuristica(pontoA):
    return (abs(pontoA[0] - pontoFinal[0]) + (abs(pontoA[1] - pontoFinal[1])))


def achaPeso(direcao):
    if (direcao == 'cima'):
        if (matriz[pontoAtual[0] - 1][pontoAtual[1]] == 0):

            return ([10 + heuristica([pontoAtual[0] - 1, pontoAtual[1]]), 'cima'])
        else:
            return ([100 + heuristica([pontoAtual[0] - 1, pontoAtual[1]]), 'cima'])
    if (direcao == 'baixo'):
        if (matriz[pontoAtual[0] + 1][pontoAtual[1]] == 0):
            return ([10 + heuristica([pontoAtual[0] + 1, pontoAtual[1]]), 'baixo'])
        else:
            return ([100 + heuristica([pontoAtual[0] + 1, pontoAtual[1]]), 'baixo'])
    if (direcao == 'esquerda'):
        if (matriz[pontoAtual[0]][pontoAtual[1] - 1] == 0):
            return ([10 + heuristica([pontoAtual[0], pontoAtual[1] - 1]), 'esquerda'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] - 1]), 'esquerda'])
    if (direcao == 'direita'):
        if (matriz[pontoAtual[0]][pontoAtual[1] + 1] == 0):
            return ([10 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'direita'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'direita'])
    if (direcao == 'cima_direita'):
        if (matriz[pontoAtual[0] - 1][pontoAtual[1] + 1] == 0):
            return ([14 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'cima_direita'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'cima_direita'])
    if (direcao == 'cima_esquerda'):
        if (matriz[pontoAtual[0] - 1][pontoAtual[1] - 1] == 0):
            return ([14 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'cima_esquerda'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'cima_esquerda'])
    if (direcao == 'baixo_direita'):
        if (matriz[pontoAtual[0] + 1][pontoAtual[1] + 1] == 0):
            return ([14 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'baixo_direita'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'baixo_direita'])
    if (direcao == 'baixo_esquerda'):
        if (matriz[pontoAtual[0] + 1][pontoAtual[1] - 1] == 0):
            return ([14 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'baixo_esquerda'])
        else:
            return ([100 + heuristica([pontoAtual[0], pontoAtual[1] + 1]), 'baixo_esquerda'])


def inserePontoInicial(pontoInicial):
    print("Insira um ponto inicial. Exemplo: X Y \n")
    pontoInicialInserido = ['', '']
    pontoInicialInserido[0] = int(input("Insira o valor X: "))
    pontoInicialInserido[1] = int(input("Insira o valor Y: "))
    print(pontoInicialInserido, "\n")
    if (pontoInicialInserido[0] != '' and pontoInicialInserido[1] != ''):
        print("Ponto Inicial passou na validação!", pontoInicialInserido)
        pontoInicial = pontoInicialInserido
    return (pontoInicial)


def inserePontoFinal(pontoFinal, pontoInicial):
    print("Agora, insira os pontos finais. Exemplo: X Y \n")
    pontoFinalInserido = ['', '']
    pontoFinalInserido[0] = int(input("Insira o valor X: "))
    pontoFinalInserido[1] = int(input("Insira o valor Y: "))
    if (pontoFinalInserido[0] != '' and pontoFinalInserido[1] != ''):
        while (pontoFinalInserido[0] == pontoInicial[0] and pontoFinalInserido[1] == pontoInicial[1]):
            print("Ponto Final igual ao ponto inicial, por favor insira outros valores.", pontoFinalInserido,
                  pontoInicial)
            pontoFinalInserido[0] = input("Insira o valor X: ")
            pontoFinalInserido[1] = input("Insira o valor Y: ")
        else:
            print("Ponto Final passou na validação!", pontoFinalInserido)
            pontoFinal = pontoFinalInserido
    return (pontoFinal)


# def inputMatrix(matriz):
#  with open('input.txt', 'r') as f:
#    l = [[int(num) for num in line.split(',')] for line in f]
#  print (l)
#  matriz = l
#  return matriz


def mover(lado):
    if lado == 'esquerda':
        return esquerda()
    if lado == 'direita':
        return direita()
    if lado == 'cima':
        return cima()
    if lado == 'baixo':
        return baixo()
    if lado == 'cima_direita':
        return cima_direita()
    if lado == 'cima_esquerda':
        return cima_esquerda()
    if lado == 'baixo_direita':
        return baixo_direita()
    else:
        return baixo_esquerda()


def ordena(matriz):
    aux = matriz[0]
    for i in matriz:
        if (aux[0] > i[0]):
            aux = i
    return (aux[1])


def imprimeMatriz(data):
    for linha in data:
        for numero in linha:
            print(f'{numero:>5}', end=" ")
        print()


def calculaCaminho(ultimaMovimentacao):
    caminhos = []
    # Ir pra cima
    if (pontoAtual[0] != 0 and ultimaMovimentacao != 'baixo'):
        caminhos.append(achaPeso('cima'))
    # Ir pra baixo
    if (pontoAtual[0] != len(matriz) - 1 and ultimaMovimentacao != 'cima'):
        caminhos.append(achaPeso('baixo'))
    # Ir pra direita
    if (pontoAtual[1] != len(matriz[0]) - 1 and ultimaMovimentacao != 'esquerda'):
        caminhos.append(achaPeso('direita'))
    # Ir pra esquerda
    if (pontoAtual[1] != 0 and ultimaMovimentacao != 'direita'):
        caminhos.append(achaPeso('esquerda'))

    # Ir para cima_direita
    if (pontoAtual[0] != 0 and pontoAtual[1] != len(matriz[0]) - 1 and ultimaMovimentacao != 'baixo_esquerda'):
        caminhos.append(achaPeso('cima_direita'))
    # Ir para cima_esquerda
    if (pontoAtual[0] != 0 and pontoAtual[1] != 0 and ultimaMovimentacao != 'baixo_direita'):
        caminhos.append(achaPeso('cima_esquerda'))
    # Ir para baixo_direita
    if (pontoAtual[0] != len(matriz) - 1 and pontoAtual[1] != len(
            matriz[0]) - 1 and ultimaMovimentacao != 'cima_esquerda'):
        caminhos.append(achaPeso('baixo_direita'))
    # Ir para baixo_esquerda
    if (pontoAtual[0] != len(matriz) - 1 and pontoAtual[1] != 0 and ultimaMovimentacao != 'cima_direita'):
        caminhos.append(achaPeso('baixo_esquerda'))

    a = ordena(caminhos)
    return (a)


def esquerda():
    if (pontoAtual[1] == 0):
        return
    else:
        pontoAtual[1] = pontoAtual[1] - 1
        return ('esquerda')


def direita():
    if (pontoAtual[1] == len(matriz[0])):
        return
    else:
        pontoAtual[1] = pontoAtual[1] + 1
        return ('direita')


def cima():
    if (pontoAtual[0] == 0):
        return
    else:
        pontoAtual[0] = pontoAtual[0] - 1
        return ('cima')


def baixo():
    if (pontoAtual[0] == len(matriz)):
        return
    else:
        pontoAtual[0] = pontoAtual[0] + 1
        return ('baixo')


def cima_direita():
    if (pontoAtual[0] == 0 or pontoAtual[1] == len(matriz)):
        return
    else:
        pontoAtual[0] = pontoAtual[0] - 1
        pontoAtual[1] = pontoAtual[1] + 1
        return ('cima_direita')


def cima_esquerda():
    if (pontoAtual[0] == 0 or pontoAtual[1] == 0):
        return
    else:
        pontoAtual[0] = pontoAtual[0] - 1
        pontoAtual[1] = pontoAtual[1] - 1
        return ('cima_esquerda')


def baixo_direita():
    if (pontoAtual[0] == len(matriz) or pontoAtual[1] == len(matriz)):
        return
    else:
        pontoAtual[0] = pontoAtual[0] + 1
        pontoAtual[1] = pontoAtual[1] + 1
        return ('baixo_direita')


def baixo_esquerda():
    if (pontoAtual[0] == len(matriz) or pontoAtual[1] == 0):
        return
    else:
        pontoAtual[0] = pontoAtual[0] + 1
        pontoAtual[1] = pontoAtual[1] - 1
        return ('baixo_esquerda')


def desenhaMatriz():
    matrizNova[pontoInicial[0]][pontoInicial[1]] = '🏃‍'
    matrizNova[pontoFinal[0]][pontoFinal[1]] = '💢'
    for i in range(len(matrizNova)):
        for j in range(len(matrizNova[0])):
            if (matrizNova[i][j] == 1):
                matrizNova[i][j] = '🚫'
            if (matrizNova[i][j] == 0):
                matrizNova[i][j] = '🔳'
            if (matrizNova[i][j] == 2):
                matrizNova[i][j] = '⬇'
            if (matrizNova[i][j] == 4):
                matrizNova[i][j] = '⬅'
            if (matrizNova[i][j] == 6):
                matrizNova[i][j] = '➡'
            if (matrizNova[i][j] == 8):
                matrizNova[i][j] = '⬆'
            if (matrizNova[i][j] == 10):
                matrizNova[i][j] = '↗'
            if (matrizNova[i][j] == 12):
                matrizNova[i][j] = '↖'
            if (matrizNova[i][j] == 14):
                matrizNova[i][j] = '↘'
            if (matrizNova[i][j] == 16):
                matrizNova[i][j] = '↙'


def copiaMatriz():
    matrizNova = []
    for i in matriz:
        matrizNova.append(i[:])
    return matrizNova


def atualizaMatriz():
    if (ultimaMovimentacao == 'baixo'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 2
    if (ultimaMovimentacao == 'cima'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 8
    if (ultimaMovimentacao == 'esquerda'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 4
    if (ultimaMovimentacao == 'direita'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 6
    if (ultimaMovimentacao == 'cima_direita'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 10
    if (ultimaMovimentacao == 'cima_esquerda'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 12
    if (ultimaMovimentacao == 'baixo_direita'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 14
    if (ultimaMovimentacao == 'baixo_esquerda'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 16


def buscaVizinhos():
    lista = []
    # Cima
    if (pontoAtual[0] != 0 and matriz[pontoAtual[0] - 1][pontoAtual[1]] == 0):
        lista.append([(pontoAtual[0] - 1)], [(pontoAtual[1])], [False])
    # Baixo
    if (pontoAtual[1] != len(matriz[0]) - 1 and matriz[pontoAtual[0] + 1][pontoAtual[1]] == 0):
        lista.append([(pontoAtual[0] + 1)], [(pontoAtual[1])], [False])
    # Esquerda
    if (pontoAtual[1] != 0 and matriz[pontoAtual[0]][pontoAtual[1] - 1] == 0):
        lista.append([int(pontoAtual[0])], [(pontoAtual[1] - 1)], [False])
    # Direita
    if (pontoAtual[1] != len(matriz[0]) - 1 and matriz[pontoAtual[0]][pontoAtual[1] + 1] == 0):
        lista.append([int(pontoAtual[0])], [(pontoAtual[1] + 1)], [False])
    # Cima Direita
    if (pontoAtual[0] != 0 and pontoAtual[1] != len(matriz[0]) - 1 and matriz[pontoAtual[0] - 1][
        pontoAtual[1] + 1] == 0):
        lista.append([(pontoAtual[0] - 1)], [(pontoAtual[1] + 1)], [True])
    # Cima Esquerda
    if (pontoAtual[0] != 0 and pontoAtual[1] != 0 and matriz[pontoAtual[0] - 1][pontoAtual[1] - 1] == 0):
        lista.append([(pontoAtual[0] - 1)], [(pontoAtual[1] - 1)], [True])
    # Baixo Direita
    if (pontoAtual[0] != len(matriz) - 1 and pontoAtual[1] != len(matriz[0]) - 1 and matriz[pontoAtual[0] + 1][
        pontoAtual[1] + 1] == 0):
        lista.append([(pontoAtual[0] + 1)], [(pontoAtual[1] + 1)], [True])
    # Baixo Esquerda
    if (pontoAtual[0] != len(matriz) - 1 and pontoAtual[1] != 0 and matriz[pontoAtual[0] + 1][pontoAtual[1] - 1] == 0):
        lista.append([(pontoAtual[0] + 1)], [(pontoAtual[1] - 1)], [True])

    return lista


def pathFinder():

    while pontoAtual != pontoFinal:
        if len(listaAberta) == 0:
            return
        pontoAtual = listaAberta.pop(0)
        listaFechada.append(pontoAtual)
        if pontoAtual == pontoFinal:
            return
        if listaAberta.count(0):
            return

        listaVizinhos = buscaVizinhos()
        for i in range(len(listaVizinhos)):
            vizinho = listaVizinhos[i]
            if vizinho in listaFechada:
                continue
            h = abs(pontoFinal[0] - vizinho[0])
            h += abs(pontoFinal[1] - vizinho[1])
            if vizinho not in listaAberta:
                if pontoAtual == pontoInicial:
                    g = 14 if vizinho[2] else 10
                else:
                    g = listaPais[2] + 14 if vizinho[2] else listaPais[2] + 10

                f = g + h
                listaPais.append([vizinho, pontoAtual, g])
                listaAberta.append(vizinho, f)
            elif vizinho in listaAberta and (vizinho[0] == pontoAtual[0] or vizinho[1] == pontoAtual[1]):
                g = listaPais[2] + 14 if vizinho[2] else listaPais[2] + 10





matriz = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

# matriz = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]]

pontoInicial = [0, 0]
pontoFinal = [4, 5]

pontoInicial = inserePontoInicial(pontoInicial)
pontoFinal = inserePontoFinal(pontoFinal, pontoInicial)
# matriz = inputMatrix(matriz)

movimentacao = []
pontoAtual = pontoInicial[:]
caminhos = []
ultimaMovimentacao = ''
matrizNova = copiaMatriz()
listaAberta = []
listaFechada = []
listaPais = []

while pontoAtual != pontoFinal:
    movimentacao.append(pontoAtual[:])
    ultimaMovimentacao = mover(calculaCaminho(ultimaMovimentacao))
    atualizaMatriz()
movimentacao.append(pontoAtual[:])
print(movimentacao)
print("\n")
desenhaMatriz()
imprimeMatriz(matrizNova)

valorF = 0

listaAberta.append(pontoInicial)
pathFinder()