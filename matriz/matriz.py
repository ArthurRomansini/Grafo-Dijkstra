from matriz.vertice import Vertice
from matriz.aresta import Aresta


class MatrizAdjacente():
    def __init__(self):
        self.__vertices = []
        self.__arestas = []
        self.__matriz = []
    
    def getVertices(self):
        return self.__vertices
    
    def getArestas(self):
        return self.__arestas
    
    def getMatriz(self):
        return self.__matriz
    
    def addVertice(self, nome, valor):
        self.__vertices.append(Vertice(nome, valor))
        self.__matriz.append([])
        for i in range(len(self.__matriz)):
            self.__matriz[i].append(0)
        for i in range(len(self.__matriz)-1):
            self.__matriz[len(self.__matriz)-1].append(0)
    
    def addAresta(self, valor, vertice1, vertice2):
        self.__arestas.append(Aresta(valor, vertice1, vertice2))
        self.__matriz[self.__vertices.index(vertice1)][self.__vertices.index(vertice2)] = valor
        self.__matriz[self.__vertices.index(vertice2)][self.__vertices.index(vertice1)] = valor
        
    def getVertice(self, nome):
        for i in self.__vertices:
            if i.getNome() == nome:
                return i
        return None
    
    def getAresta(self, vertice1, vertice2):
        for i in self.__arestas:
            if i.getVertice1() == vertice1 and i.getVertice2() == vertice2:
                return i
        return None
    
    def getArestasVertice(self, vertice):
        arestas = []
        for i in self.__arestas:
            if i.getVertice1() == vertice or i.getVertice2() == vertice:
                arestas.append(i)
        return arestas
    
    def getVerticesAresta(self, aresta):
        return aresta.getVertices()
    
    def getValorAresta(self, aresta):
        return aresta.getValor()
    
    def getValorVertice(self, vertice):
        return vertice.getValor()
    


            

           
