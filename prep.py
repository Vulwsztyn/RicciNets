import networkx as nx
import numpy as np
from nodemass import undirected_to_dag


def prepare_new_graph_2(directed_graph, isolated_nodes):
  new_graph = nx.Graph()
  new_edges = directed_graph.edges()
  top_node = (len(list(directed_graph.nodes())) - 1)
  isolated_nodes.append(0) if 0 not in isolated_nodes else isolated_nodes
  isolated_nodes.append(top_node) if top_node not in isolated_nodes else isolated_nodes
  directed_graph.remove_nodes_from(isolated_nodes)
  new_nodes = (list(directed_graph.nodes()))
  new_nodes = list(np.subtract(new_nodes,1))
  new_edges = [tuple(np.subtract(x, (1,1))) for x in directed_graph.edges()]
  new_graph.add_nodes_from(new_nodes)
  new_graph.add_edges_from(new_edges)
  new_undirected_graph = nx.convert_node_labels_to_integers(new_graph)
  return new_undirected_graph

def prepare_new_graph(directed_graph):
  G = directed_graph.to_undirected()
  H = undirected_to_dag(G)
  H = H.to_undirected()
  return H