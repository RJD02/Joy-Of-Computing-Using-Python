import networkx as nx
import numpy

G = nx.read_edgelist('facebook_combined.txt')
N = list(G.nodes())

spll = []

for u in N:
    for v in N:
        if u == v:
            continue
        l = nx.shortest_path_length(G, u, v)
        print('Shortest Path between', u, 'and', v, 'is of length',l)
        spll.append(l)

min_spl = min(spll)
max_spl = max(spll)
print('Minimum shortest path length is:', min_spl)
print('Maximum shortest path length is:', max_spl)
avg_spl = numpy.average(spll)
print('Average shortest path length is:', avg_spl)
