# CNS186_Monocular_Depth


Papers:
- https://arxiv.org/pdf/1609.03677v3.pdf
  - Code: https://github.com/mrharicot/monodepth

Proposal:
•Framework: Unsupervised CNN (Encoder / Decoder type architecture) trained with stereo images.
Predicts disparity maps between L/R stereo pairs to produce predicted opposite image in the pair (towards depth estimation calculation)

•Loss Function: Constrain the appearance matching, disparity smoothness and Left-Right disparity consistency

•Datasets: KITTI dataset; Make3D, NYU-Depth V2(if needed)

•Expected Results: Achieve comparable results with reference paper and other existing supervised methods for depth estimation
