import copy
class GraphUtils:

    def buscaLargura(_self, origem, destino, grafo, pai):
        visitado = [False] * len(grafo)
        fila = []
        fila.append(origem)
        visitado[origem] = True

        while fila:
            v = fila.pop(0)
            for u in range(len(grafo[v])):
                if (grafo[v][u] == 1 and not visitado[u]):
                    fila.append(u)
                    visitado[u] = True
                    pai[u] = v

        return visitado[destino]

    def buscaProfundidade(_self, origem, destino, grafo, visitado, caminho, caminhos):
        visitado[origem] = True
        caminho.append(origem)

        if origem == destino:
            caminhos.append(copy.deepcopy(caminho))
        else:
            for i in range(len(grafo)):
                if (grafo[origem][i] == 1 and visitado[i] == False):
                    _self.buscaProfundidade(i, destino, grafo, visitado, caminho, caminhos)
        
        caminho.pop()
        visitado[origem] = False

    def comp(_self, l1, l2):
        for i in l1:
            if i in l2:
                return True

        return False

    def acharCaminhos(_self, origem, destino, grafo, n, cam_dis):
        visitado = [False] * len(grafo)
        caminho = []
        caminhos = []
        
        _self.buscaProfundidade(origem, destino, grafo, visitado, caminho, caminhos)
        disjuntos = []
        for caminhoA in caminhos:
            disjuntos = [caminhoA]
            aDuplas = []
            for i in range(len(caminhoA[:-1])):
                aDuplas.append((caminhoA[i], caminhoA[i+1]))
            
            posA = caminhos.index(caminhoA)+1

            visitados = copy.deepcopy(aDuplas)
            for caminhoB in caminhos[posA:]:
                bDuplas = []
                
                for i in range(len(caminhoB[:-1])):
                    bDuplas.append((caminhoB[i], caminhoB[i+1]))

                if _self.comp(visitados, bDuplas) == False:
                    disjuntos.append(caminhoB)
                    visitados.extend(bDuplas)

            if len(disjuntos) == n:
                with open(cam_dis, 'w') as f:
                    for i in disjuntos:
                        f.write(str(i) + "\n")
                return disjuntos


        print("acharCaminhos num: ", len(disjuntos))
        
        return []
    
    def caminhosDisjuntos(_self, origem, destino, g, cam_dis):
        grafo = copy.deepcopy(g)
        pai = [-1] * len(grafo)
        fluxo_maximo = 0
        while (_self.buscaLargura(origem, destino, grafo, pai)):
            fluxo_caminho = float("Inf")
            v = destino
            while (v != origem):
                fluxo_caminho = min(fluxo_caminho, grafo[pai[v]][v])
                v = pai[v]

            fluxo_maximo += fluxo_caminho
            v = destino

            while (v != origem):
                u = pai[v]
                grafo[u][v] -= fluxo_caminho
                grafo[v][u] += fluxo_caminho
                v = pai[v]

        dif = _self.difMatriz(g, grafo)

        _self.acharCaminhos(origem, destino, dif, fluxo_maximo, cam_dis)
        
        return fluxo_maximo
            
    def getGrafo(_self, arq):
        data = []
        file = open(arq, "r")

        data = [l for l in file.readlines()]
        for i in range(len(data)):
            data[i] = [eval(k) for k in data[i][:-1]]

        file.close()
        return data

    def printGrafo(_self, grafo):
        for i in grafo:
            for j in i:
                print(j, end=" ")

            print("")

    def difMatriz(_self, grafo, fluxo):
        g = copy.deepcopy(grafo)
        for i in range(len(g)):
            for j in range(len(g[i])):
                if (fluxo[i][j] != 0):
                    g[i][j] = 0
        
        return g
