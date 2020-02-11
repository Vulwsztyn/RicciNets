import matplotlib.pyplot as plt
import networkx as nx

def show_results(G):
    # Print the first five results
    print("First 5 edges: ")
    for n1,n2 in list(G.edges())[:5]:
        print("Ollivier-Ricci curvature of edge (%s,%s) is %f" % (n1 ,n2, G[n1][n2]["ricciCurvature"]))

    # Plot the histogram of Ricci curvatures
    plt.subplot(2, 1, 1)
    ricci_curvtures = nx.get_edge_attributes(G, "ricciCurvature").values()
    plt.hist(ricci_curvtures,bins=20)
    plt.xlabel('Ricci curvature')
    plt.title("Histogram of Ricci Curvatures (Karate Club)")

    # Plot the histogram of edge weights
    plt.subplot(2, 1, 2)
    weights = nx.get_edge_attributes(G, "weight").values()
    plt.hist(weights,bins=20)
    plt.xlabel('Edge weight')
    plt.title("Histogram of Edge weights (Karate Club)")

    plt.tight_layout()
    plt.show()
   
def draw_graph(G):
    """
    A helper function to draw a nx graph with community.
    """
    groups =nx.get_node_attributes(G,'club').values()
    color_list = plt.cm.tab10(np.linspace(0, 1, len(groups)))
    color_dict = dict(zip(groups, color_list))
        
    nx.draw_spring(G,seed=0, nodelist=G.nodes(),
                   node_color=[color_dict[x] for x in groups],
                   alpha=0.8)
    
