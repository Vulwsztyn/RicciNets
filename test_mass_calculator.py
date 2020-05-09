import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from nodemass import undirected_to_dag
#plt.clf()
#G = nx.watts_strogatz_graph(10,5,0.5)
#H = undirected_to_dag(G)
#plt.clf()
#nx.draw(H)
#nx.draw_shell(H, with_labels=True)
#plt.show()
#plt.clf()

#hub_node = 2
#alpha = 0.5
#beta = 1
#delta = 0


def get_single_node_neighbor_distributions(G, hub_node, alpha, beta, delta):
	predecessors = list(G.predecessors(hub_node))
	successors = list(G.successors(hub_node))
	n_I = len(predecessors)
	n_O = len(successors)
	hub_mass = (1 - beta * (1 - alpha) + (n_O + n_I) * (n_O/n_I) * delta * (1 - 1/n_I)) if n_I != 0 else (alpha)
	neighbors = predecessors + successors
	predecessor_mass = []
	successor_mass = []
	for node in neighbors:
		if node in predecessors:
			predecessor_mass.append((1 - hub_mass)/n_I)
		elif node in successors:
			successor_mass.append((1 - hub_mass)/n_O)
	predecessor_mass.append(hub_mass)
	successor_mass.append(hub_mass)
	return predecessor_mass, successor_mass

def get_density_distribution(G,alpha,beta,delta):
	densities = dict()
	for x in G.nodes():
		dist = (get_single_node_neighbor_distributions(G,x,alpha,beta,delta))
		densities[x] = {"predecessors" : dist[0], "successors" : dist[1]}
	return densities

#A = get_density_distribution(H,0.5,1,0)
#print(A[6]["predecessors"])
