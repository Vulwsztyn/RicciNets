# Take graph that has been ricci flowed and chop out all the edges that are outside a range
import networkx as nx

def surgery(directed_graph, upper_bound, lower_bound):
    for n1,n2 in list(directed_graph.edges()):
        if not (lower_bound <= (directed_graph[n1][n2]["weight"]) <= upper_bound):
            directed_graph.remove_edge(n1,n2)
            print('removed edge {}, {}'.format(n1,n2))
    return directed_graph
	#print(upper_bound)
	#print(lower_bound)




                