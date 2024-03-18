from pyvis.network import Network
import networkx as nx

nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]["title"] = "Number 1"

nt = Network("500px", "500px")
