import networkx as nx

# Crear un grafo con las conexiones entre los puntos
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

# Calcular la ruta más corta entre dos puntos
shortest_path = nx.shortest_path(G, source='A', target='D', weight='weight')
shortest_path_length = nx.shortest_path_length(G, source='A', target='D', weight='weight')

print("La ruta más corta es:", shortest_path)
print("La longitud de la ruta más corta es:", shortest_path_length)

