import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basins with chaotic modulation
        radial = np.sum((x_norm**2) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Chaotic sine wave components with exponential decay
        chaotic = np.sum(np.sin(10 * np.pi * x_norm * np.exp(-0.1 * np.sum(x_norm**2))) * 
                        np.exp(-0.2 * x_norm**2))
        
        # Cross-dimensional coupling with radial symmetry
        coupling = np.sum(np.sin(5 * np.pi * np.sqrt(x_norm[:-1]**2 + x_norm[1:]**2)) * 
                         np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Multi-scale oscillations with varying amplitudes
        multi_scale = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                            np.exp(-0.1 * x_norm**2))
        
        # Asymmetric saddle points with logarithmic spacing
        asymmetric = np.sum(np.tanh(2 * x_norm[:-1]) * np.tanh(2 * x_norm[1:]) * 
                           (x_norm[:-1]**3 - x_norm[1:]**3))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all terms
        return condition_factor * (radial + chaotic + coupling + multi_scale + asymmetric)