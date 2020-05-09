import networkx as nx
import numpy as np
import math
import importlib
from matplotlib import animation
# matplotlib setting
#%matplotlib inline
import matplotlib.pyplot as plt

# to print logs in jupyter notebook
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

# load GraphRicciCuravture package
from GraphRicciCurvature.OllivierRicci import OllivierRicci

from nodemass import undirected_to_dag
from surgery import surgery
from display import show_results
from animate_surgery import simple_update, simple_animation

G = nx.watts_strogatz_graph(32,4,0.75)
H = undirected_to_dag(G)

plt.clf()
nx.draw_shell(H, with_labels=True)
plt.savefig('Hstart.png')


orc = OllivierRicci(H, alpha=0.5, beta=1, delta=0, base=1, exp_power=0, proc=4, verbose="INFO")
G_orc = orc.G.copy()
orf = OllivierRicci(H, alpha=0.5, beta=1, delta=0, base=1, exp_power=0, proc=4, verbose="INFO")
orf.compute_ricci_flow(iterations=50)
G_rf = orf.G.copy(G)
