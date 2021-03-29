import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# Adding nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
# Adding Edges
G.add_edge(1, 3)
G.add_edge(1, 2)
G.add_edge(2, 3)
# Showing Nodes
print(G.nodes())
# Showing Edges
print(G.edges())
# Drawing the complete graph
nx.draw(G)
# Plotting on graph
plt.show()

# Using complete_graph method
H = nx.complete_graph(10)
nx.draw(H)
plt.show()
