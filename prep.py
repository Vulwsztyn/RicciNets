import networkx as nx
import numpy as np
from nodemass import undirected_to_dag

# Prepare a dag for feeding back into RandWire, ie. undirected remove input and output nodes
def prepare_new_graph(directed_graph, isolated_nodes):
  # Make new graph
  new_graph = nx.Graph()
  # Copy edges from directed graph
  new_edges = directed_graph.edges()
  # Get label of highest node
  top_node = (len(list(directed_graph.nodes())) - 1)
  # Make sure input and output nodes will be removed even if they are not isolated
  isolated_nodes.append(0) if 0 not in isolated_nodes else isolated_nodes
  isolated_nodes.append(top_node) if top_node not in isolated_nodes else isolated_nodes
  # Remove all isolated nodes
  directed_graph.remove_nodes_from(isolated_nodes)
  # Copy nodes and edges to new graph
  new_nodes = (list(directed_graph.nodes()))
  new_nodes = list(np.subtract(new_nodes,1))
  # Relabel edges
  new_edges = [tuple(np.subtract(x, (1,1))) for x in directed_graph.edges()]
  # Copy nodes and edges
  new_graph.add_nodes_from(new_nodes)
  new_graph.add_edges_from(new_edges)
  # Make sure labels start at 0
  new_undirected_graph = nx.convert_node_labels_to_integers(new_graph)
  return new_undirected_graph
