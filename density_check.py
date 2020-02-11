import networkx as nx
import time



def undirected_to_dag(undirected_graph):
	directed_graph = nx.DiGraph()
	for i in range(len(list(undirected_graph))):
		neighbors = list(undirected_graph.neighbors(i))
		count = len([k for k in neighbors if k > i])
		if count == 0:
			directed_graph.add_edge(i,list(undirected_graph)[-1])			
		for n in neighbors:
			if n > i:
				directed_graph.add_edge(i, n)
			elif i > n:
				directed_graph.add_edge(n, i)
	return directed_graph
	
G = nx.karate_club_graph()
lengths_G = dict(nx.all_pairs_dijkstra_path_length(G))	
H = undirected_to_dag(G)
lengths_H = dict(nx.all_pairs_dijkstra_path_length(H))

# All my graphs have to b directed so I can get rid of all the if statements pertaining to directed/undirected

def _get_edge_density_distributions(_G, _alpha, _base, _apsp, _exp_power):
    """
    Pre-compute densities distribution for all edges.
    """

    densities = dict()
    EPSILON = 0.00000000000000001
    t0 = time.time()

    # Construct the density distributions on each node
    def get_single_node_neighbors_distributions(neighbors, direction="successors"):

        # Get sum of distributions from x's all neighbors
        # Leave in the probability distribution for now
        if direction == "predecessors":
            nbr_edge_weight_sum = sum([_base ** (-(_apsp[nbr][x]) ** _exp_power)
                                       for nbr in neighbors])
        else:
            nbr_edge_weight_sum = sum([_base ** (-(_apsp[x][nbr]) ** _exp_power)
                                       for nbr in neighbors])

        if nbr_edge_weight_sum > EPSILON:
            if direction == "predecessors":
                result = [(1.0 - _alpha) * (_base ** (-(_apsp[nbr][x]) ** _exp_power)) /
                          nbr_edge_weight_sum for nbr in neighbors]
            else:
                result = [(1.0 - _alpha) * (_base ** (-(_apsp[x][nbr]) ** _exp_power)) /
                          nbr_edge_weight_sum for nbr in neighbors]
        elif len(neighbors) == 0:
            return []
        else:
            result = [(1.0 - _alpha) / len(neighbors)] * len(neighbors)
        result.append(_alpha)
        return result

    if _G.is_directed():
        for x in _G.nodes():
            predecessors = get_single_node_neighbors_distributions(list(_G.predecessors(x)), "predecessors")
            successors = get_single_node_neighbors_distributions(list(_G.successors(x)))
            densities[x] = {"predecessors": predecessors, "successors": successors}
    else:
        for x in _G.nodes():
            densities[x] = get_single_node_neighbors_distributions(list(_G.neighbors(x)))

    #logger.info("%8f secs for edge density distribution construction" % (time.time() - t0))
    return densities
    
#print(nx.info(G))

# Testing with undirected Graphs

density_dist_H = _get_edge_density_distributions(H, 0.5, 1, lengths_H, 0)
#density_dist_G = _get_edge_density_distributions(G, 0.5, 1, lengths, 0)
print(density_dist_H[2]["predecessors"])
# This gives a list of weights of masses of predecessor nodes to 2 follow by the mass of node 2
print(density_dist_H[2]["successors"])
# This gives a list of weights of masses of successor nodes to 2 followed by the mass of 2
print(list(H.predecessors(2)))
print(list(H.successors(2)))
#print(density_dist_G[2])
#print(list(G.neighbors(2)))
#print(lengths_G[3][2])
#print(lengths_H[2][3])


