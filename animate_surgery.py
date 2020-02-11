import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
from surgery import surgery

def simple_update(num,layout, G, ax, lower_bound, upper_bound):
	# Function just chops and plots
	ax.clear()
	H = surgery(G, upper_bound - (num*0.05), lower_bound)
	nx.draw(H, pos=layout, ax=ax, with_labels=True)
	ax.set_title("Chop above w = {}".format(upper_bound - (num*0.05)))
	
def simple_animation(G, lower_bound, upper_bound, no_frames, filename):
	fig,ax = plt.subplots(figsize=(12,10))
	layout = nx.spring_layout(G)
	ani = animation.FuncAnimation(fig, simple_update, frames=no_frames, fargs=(layout,G,ax,lower_bound, upper_bound))
	ani.save('{}_2.mp4'.format(filename), writer='imagemagick')
	plt.show()
	
