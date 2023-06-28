class Aresta():
    def __init__(self, valor, vertice1, vertice2):
        self.__valor = valor
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
    def getValor(self):
        return self.__valor
    def getVertice1(self):
        return self.__vertice1
    def getVertice2(self):
        return self.__vertice2
    def getVertices(self):
        return [self.__vertice1, self.__vertice2]
    