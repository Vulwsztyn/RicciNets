import networkx as nx
import numpy as np
from mass_calculator import get_single_node_neighbor_distributions, get_density_distribution
from nodemass import undirected_to_dag



G = nx.watts_strogatz_graph(10,5,0.5)
H = undirected_to_dag(G)

lengths = dict(nx.all_pairs_dijkstra_path_length(H))

def _distribute_densities(G, apsp, source, target, alpha, beta, delta):
    """
    Get the density distributions of source and target node, and the cost (all pair shortest paths) between
    all source's and target's neighbors.
    :param source: Source node.
    :param target: Target node.
    :return: (source's neighbors distributions, target's neighbors distributions, cost dictionary).
    """

    # Append source and target node into weight distribution matrix x,y
    source_nbr = list(G.predecessors(source))
    target_nbr = list(G.successors(target))
    
    densities = get_density_distribution(G, alpha, beta, delta)
    
    # Distribute densities for source and source's neighbors as x
    if not source_nbr:
        source_nbr.append(source)
        x = [1]
    else:
        source_nbr.append(source)
        x = densities[source]["predecessors"]

    # Distribute densities for target and target's neighbors as y
    if not target_nbr:
        target_nbr.append(target)
        y = [1]
    else:
        target_nbr.append(target)
        y = densities[target]["successors"]

    # construct the cost dictionary from x to y
    d = np.zeros((len(x), len(y)))

    for i, src in enumerate(source_nbr):
        for j, dst in enumerate(target_nbr):
            assert dst in apsp[src], \
                "Target node not in list, should not happened, pair (%d, %d)" % (src, dst)
            d[i][j] = apsp[src][dst]

    x = np.array([x]).T  # the mass that source neighborhood initially owned
    y = np.array([y]).T  # the mass that target neighborhood needs to received

    return x, y, d

print(_distribute_densities(H,lengths,2,6, 0.5, 1, 0))