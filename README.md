# Part III Project - RicciNets: Curvature-guided pruning of high-performance neural networks
The GitHub repository for my Part III Project on compact neural architecture search.

![Cavendish Crocodile](https://www.phy.cam.ac.uk/history/historypictures/crocodile_brickwork_col.gif)

The code can be run in Colaboratory, following "PartIIIProject.ipynb". This requires the other scripts here to be saved to a Google Drive. They can also be imported from Github with minor alterations to the Jupyter notebook.

The project uses a curvature-guided diffusion process, Ricci flow, to prune a graph before mapping it to a network, reducing computational demand without degradation in performance before training.

The implementation of RandWireNN used is linked here, and is unchanged (aside from choice of number of epochs).

GraphRicciCurvature is branched (ensure PartIII branch) from C.C. Ni, and slight changes of mass distribution and accepting directed graphs are made. 

Animation_2.mp4 (or .gif) show the methodology sweeping through a weight threshold and removing edges with weights outside this threshold.

Results are discussed in my report and the figures can be found here.
