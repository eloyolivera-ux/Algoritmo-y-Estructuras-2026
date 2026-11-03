from graph import Graph
from star_wars_data import personajes

grafo = Graph(is_dir=False)

for personaje in personajes:
    grafo.add_vertex(personaje['nombre'], personaje['episodios'])

for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        juntos = set(personajes[i]['episodios']) & set(personajes[j]['episodios'])
        if len(juntos) > 0:
            grafo.add_edge(len(juntos), personajes[i]['nombre'], personajes[j]['nombre'])

input('\nPresioná Enter para continuar...')

for personaje in ['C3PO', 'Yoda', 'Leia']:
    arbol = grafo.kruskal(personaje)
    print(f'\nÁrbol de expansión mínimo desde {personaje}:')

    peso_total = 0
    for arista in arbol.split(';'):
        origen, destino, peso = arista.split('-')
        print(f'{origen} - {destino} (episodios: {peso})')
        peso_total += int(peso)

    print(f'peso total: {peso_total}')

input('\nPresioná Enter para continuar...')

maximo = 0
for vertice in grafo:
    for arista in vertice.edges:
        if arista.weight > maximo:
            maximo = arista.weight

print(f'\nMáximo de episodios compartidos: {maximo}')

print('Pares de personajes que lo comparten:')
for vertice in grafo:
    for arista in vertice.edges:
        if arista.weight == maximo and vertice.value < arista.destination:
            print(f'{vertice.value} - {arista.destination}')

input('\nPresioná Enter para continuar...')

for origen, destino in [('C3PO', 'R2D2'), ('Yoda', 'Darth Vader')]:
    caminos = grafo.dijkstra(origen)

    buscado = destino
    peso_total = None
    camino = []

    while caminos.size() > 0:
        valor = caminos.pop()
        if valor[0] == buscado:
            if peso_total is None:
                peso_total = valor[1]
            camino.append(valor[0])
            buscado = valor[2]

    camino.reverse()
    print(f'\nCamino más corto de {origen} a {destino}: {" - ".join(camino)}')
    print(f'costo total: {peso_total}')

input('\nPresioná Enter para continuar...')

print('\nPersonajes que aparecieron en los 9 episodios:')
for vertice in grafo:
    if len(vertice.other_values) == 9:
        print(vertice.value)
        