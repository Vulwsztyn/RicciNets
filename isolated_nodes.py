import networkx as nx
# Function to return the list of nodes in a graph with no connected edges
def get_isolated_nodes(directed_graph):
    isolated_nodes = []
    for node in list(directed_graph.nodes()):
        if not directed_graph.predecessors(node):
            if not directed_graph.successors(node):
                isolated_nodes.append(node)
    return isolated_nodes
