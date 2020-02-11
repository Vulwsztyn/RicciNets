# PartIIIProject
Repo for my Part III Project, Training High Performance Compact Neural Networks

Meeting 10/02/20
- Looked back over research proposal
- Looked at animation_2.mp4 that shows the pruning of edges under a decreasing weight threshold
  - Weights calculate from process of Ricci Flow in OllivierRicci2.py
  - getgoing.py initialises graph used in RandWire (32,4,0.75) and calculates edge weights using alpha = 0.5 (proportion of mass left on hub node), beta = 1 (hyperparameter controlling contribution of community detection term) and delta = 0 (hyperparameter controlling robustness and computational demand terms)
- Update Github
- Get RandWireNN running
