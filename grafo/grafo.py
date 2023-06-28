from matriz.matriz import MatrizAdjacente
from fila.filaPrioridade import FilaPrioridade
            

class Grafo():
    def __init__(self):
        self.__matriz = MatrizAdjacente()
        
    def getMatriz(self):
        return self.__matriz
    
    def addVertice(self, nome, valor):
        self.__matriz.addVertice(nome, valor)
    
    def addAresta(self, valor, vertice1, vertice2):
        self.__matriz.addAresta(valor, vertice1, vertice2)
    
    def getVertice(self, nome):
        return self.__matriz.getVertice(nome)
    
    def getAresta(self, vertice1, vertice2):
        return self.__matriz.getAresta(vertice1, vertice2)
    
    def printGrafo(self):
        for i in self.__matriz.getVertices():
            print(i.getNome(), i.getValor())
        for i in self.__matriz.getArestas():
            print(i.getValor(), i.getVertice1().getNome(), i.getVertice2().getNome())

    def dijkstra(self, origem):
        distancias = {vertice: float('inf') for vertice in self.__matriz.getVertices()}
        distancias[origem] = 0

        fila_prioridade = FilaPrioridade()
        fila_prioridade.put((0, origem), 0)

        while not fila_prioridade.empty():
            distancia_atual, vertice_atual = fila_prioridade.get()

            for aresta in self.__matriz.getArestasVertice(vertice_atual):
                vizinho = aresta.getVertices()[1]
                distancia = distancias[vertice_atual] + aresta.getValor()

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    fila_prioridade.put((distancia, vizinho), distancia)

        return distancias
            
            