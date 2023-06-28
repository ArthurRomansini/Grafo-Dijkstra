from grafo.grafo import Grafo

# Criado por: Arthur Romansini Fernandes e Luiz Antonio de Souza Cardoso

""" 
    matriz = {
        'Criciuma': ['Sidelopolis', 'Içara']
        'Sidelopolis': ['Criciuma', 'Içara', 'Lages']
        'Içara': ['Criciuma', 'Sidelopolis', 'Curitiba', 'Tubarao']
        'Lages': ['Sidelopolis', 'Curitiba', 'Sorocaba', 'Florianopolis']
        'Curitiba': ['Içara', 'Lages', 'Tubarao']
        'Tubarao': ['Içara', 'Curitiba', 'Florianopolis']
        'Sorocaba': ['Lages', 'Florianopolis', 'Sao Paulo']
        'Florianopolis': ['Tubarao', 'Lages', 'Sorocaba', 'Sao Paulo']
        'Sao Paulo' : ['Sorocaba', 'Florianopolis']
    }
"""

grafo1 = Grafo()

grafo1.addVertice('Criciuma', 1)
grafo1.addVertice('Sidelopolis', 2)
grafo1.addVertice('Içara', 3)
grafo1.addVertice('Lages', 4)
grafo1.addVertice('Curitiba', 5)
grafo1.addVertice('Tubarao', 6)
grafo1.addVertice('Sorocaba', 7)
grafo1.addVertice('Florianopolis', 8)
grafo1.addVertice('Sao Paulo', 9)

print('\n')

grafo1.addAresta(4, grafo1.getVertice('Criciuma'), grafo1.getVertice('Sidelopolis')) 
grafo1.addAresta(8, grafo1.getVertice('Criciuma'), grafo1.getVertice('Içara'))
grafo1.addAresta(11, grafo1.getVertice('Sidelopolis'), grafo1.getVertice('Içara'))
grafo1.addAresta(8, grafo1.getVertice('Sidelopolis'), grafo1.getVertice('Lages'))
grafo1.addAresta(7, grafo1.getVertice('Içara'), grafo1.getVertice('Curitiba'))
grafo1.addAresta(1, grafo1.getVertice('Içara'), grafo1.getVertice('Tubarao'))
grafo1.addAresta(2, grafo1.getVertice('Lages'), grafo1.getVertice('Curitiba'))
grafo1.addAresta(7, grafo1.getVertice('Lages'), grafo1.getVertice('Sorocaba'))
grafo1.addAresta(4, grafo1.getVertice('Lages'), grafo1.getVertice('Florianopolis'))
grafo1.addAresta(6, grafo1.getVertice('Curitiba'), grafo1.getVertice('Tubarao'))
grafo1.addAresta(2, grafo1.getVertice('Tubarao'), grafo1.getVertice('Florianopolis'))
grafo1.addAresta(14, grafo1.getVertice('Sorocaba'), grafo1.getVertice('Florianopolis'))
grafo1.addAresta(9, grafo1.getVertice('Sorocaba'), grafo1.getVertice('Sao Paulo'))
grafo1.addAresta(10, grafo1.getVertice('Florianopolis'), grafo1.getVertice('Sao Paulo'))
grafo1.addAresta(6, grafo1.getVertice('Tubarao'), grafo1.getVertice('Curitiba'))


grafo1.printGrafo()

print('\n')

origem = grafo1.getVertice('Criciuma')
distancias = grafo1.dijkstra(origem)

for vertice, distancia in distancias.items():
    print(f'Distância de {origem.getNome()} até {vertice.getNome()}: {distancia}')