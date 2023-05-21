import random
class RandomGraphs:
    def salvarGrafo(_self, grafo, arq):
        with open(arq, 'w') as file:
            for i in range(len(grafo)):
                for j in range(len(grafo)):
                    file.write(str(grafo[i][j]))
                file.write("\n")

    def grafoAleatorio(_self, n, p):
        grafo = [[]]*n
        for i in range(n):
            grafo[i] = [0]*n
            for j in range(n):
                if (j != i):
                    probability = random.random()
                    if (probability < p):
                        grafo[i][j] = 1

        return grafo
    
    def gerarGrafoCiclico(_self, n):
        grafo = []
        for i in range(n):
            grafo.append([0] * n)
            grafo[i][(i+1)%n] = 1

        return grafo

    def gerarGrafoCompleto(_self, n):
        return _self.grafoAleatorio(n, 1)