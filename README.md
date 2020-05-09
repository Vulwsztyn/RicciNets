# Part III Project - RicciNets: Curvature-guided pruning of high-performance neural networks
The GitHub repository for my Part III Project on compact neural architecture search.

The code can be run in Colaboratory, following "PartIIIProject.ipynb". This requires the other scripts here to be saved to a Google Drive. They can also be used from Github with minor alterations.

The project uses a curvature-guided diffusion process, Ricci flow, to prune a graph before mapping it to a network.


Meeting 10/02/20
- Looked back over research proposal
- Looked at animation_2.mp4 that shows the pruning of edges under a decreasing weight threshold
  - Weights calculate from process of Ricci Flow in OllivierRicci2.py
  - getgoing.py initialises graph used in RandWire (32,4,0.75) and calculates edge weights using alpha = 0.5 (proportion of mass left on hub node), beta = 1 (hyperparameter controlling contribution of community detection term) and delta = 0 (hyperparameter controlling robustness and computational demand terms)
- Update Github
- Get RandWireNN running
