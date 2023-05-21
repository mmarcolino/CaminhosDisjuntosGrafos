import time
import sys
import argparse
from service.graphUtils import GraphUtils
from service.randomGraph import RandomGraphs

gu = GraphUtils()
rg = RandomGraphs()
v = 10
p = 0.3
grafo = []
cam_dir = "./disjuntos.txt"
origem = 0
destino = v - 1

random = input("Deseja inserir p número de vértices do grafo? 1 para sim, 0 para não: ")
graph_type = int(input("Digite 1 para um grafo qualquer, 2 para um grafo ciclico ou 3 para um grafo completo: "))

if (random != 0):
    v = int(input("Insira o número de vértices: "))
    

sys.setrecursionlimit(100000)
start = time.time()

if (graph_type != 1):
    if (graph_type == 2):
        grafo = rg.gerarGrafoCiclico(v)
        rg.salvarGrafo(grafo, "resources\ciclicGraphs.txt")
    else:
        grafo = rg.gerarGrafoCompleto(v)
        rg.salvarGrafo(grafo, "resources\completeGraphs.txt")
else:
    grafo = rg.grafoAleatorio(v, p)
    rg.salvarGrafo(grafo, "resources\simpleGraph.txt")

numCaminhosDisjuntos = gu.caminhosDisjuntos(origem, destino, grafo, cam_dir)
print("Número de caminhos: ", numCaminhosDisjuntos)

end = time.time()
print("Tempo de execucação: ", (end - start) * 10**3, "ms")
with open(cam_dir, "a") as f:
    f.write("Número de caminhos: " + str(numCaminhosDisjuntos) + "\n")
    f.write("Tempo de execucação: " + str((end - start) * 10**3) +  "ms\n")