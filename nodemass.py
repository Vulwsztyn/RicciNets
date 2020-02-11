import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
#G.add_edges_from([('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E','F'), ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G'), ('Q', 'D')])

densities = dict()

def get_node_properties(node_label, directed_graph):
    input_degree = len(list(nx.DiGraph.predecessors(directed_graph,node_label)))
    output_degree = len(list(nx.DiGraph.successors(directed_graph,node_label)))
    total_degree = input_degree + output_degree
    node_properties = {"input degree":input_degree, "output degree":output_degree, "total degree":total_degree}
    return node_properties
    
def get_node_mass(node_label, directed_graph, alpha, beta, gamma, delta):
	node_properties = get_node_properties(node_label, directed_graph)
	if node_properties["input degree"] == 0:
		node_mass = (1 - alpha) * (beta*(1/node_properties["total degree"]) + gamma*node_properties["input degree"])	
	else:
		node_mass = (1 - alpha) * (beta*(1/node_properties["total degree"]) + gamma*node_properties["input degree"] + delta*(node_properties["output degree"]/node_properties["input degree"]))
	return node_mass

def get_densities(directed_graph):
	for x in directed_graph.nodes():
#	print(x)
		densities[x] = get_node_mass(x,G,0.5,0.5,0.5,0.5)
	return densities
	
def undirected_to_dag(undirected_graph):
	directed_graph = nx.DiGraph()
	for i in range(len(list(undirected_graph))):
		neighbors = list(undirected_graph.neighbors(i))	
		for n in neighbors:
			if n > i:
				directed_graph.add_edge(i, n)
			elif i > n:
				directed_graph.add_edge(n, i)
	for m in range(len(list(undirected_graph))):
		n_O = len(list(directed_graph.successors(m)))
		n_I = len(list(directed_graph.predecessors(m)))
		if n_O == 0:
			directed_graph.add_edge(m,len(list(undirected_graph)))
		if n_I == 0:
			directed_graph.add_edge(0, m)
	directed_graph.remove_edges_from(nx.selfloop_edges(directed_graph))
	return directed_graph


H = nx.watts_strogatz_graph(10,5,0.5)
#for i in range(len(list(H))):
#	neighbors = list(H.neighbors(i))
#	for n in neighbors:
#		if n>i:
#			G.add_edge(i,n)
#		elif n < i:
#			G.add_edge(n,i)
plt.clf()
#nx.draw(H)
nx.draw_shell(H, with_labels=True)
plt.savefig('H.png')

G = undirected_to_dag(H)
plt.clf()
#nx.draw(G)
nx.draw_shell(G, with_labels=True)
plt.savefig('G.png')
#plt.clf()
#B_properties = get_node_properties('B', G)
#B_mass = get_node_mass('B', G, 0.5,0.5,0.5,0.5)

#print(B_mass)

#print(densities)