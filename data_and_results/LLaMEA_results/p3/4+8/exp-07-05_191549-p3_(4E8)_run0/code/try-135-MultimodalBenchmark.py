import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter modulation
        tent = np.sum(1.0 - 2.0 * np.abs(x_norm - 0.5))
        
        # Spherical harmonic components with varying degrees and orders
        sph_harm = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                         np.sin(5 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Saddle-point structure with varying curvature
        saddle = np.sum((x_norm**2 - 1)**2 * (x_norm**2 - 0.5)**2)
        
        # Mixed polynomial and trigonometric terms with adaptive scaling
        mixed = np.sum(0.5 * x_norm**6 + 0.3 * np.sin(7 * np.pi * x_norm) * 
                      np.cos(5 * np.pi * x_norm) + 0.2 * x_norm**4)
        
        # Asymmetric barrier with multiple local minima
        barrier = np.sum(np.exp(-2.0 * (x_norm - 0.3)**2) + 
                        0.5 * np.exp(-1.5 * (x_norm + 0.4)**2) + 
                        0.3 * np.exp(-3.0 * (x_norm - 0.6)**2))
        
        # Coupling term with non-separable interaction
        coupling = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                         np.exp(-0.5 * x_norm**2) * (x_norm**3 + 0.1 * x_norm))
        
        # Combined objective with weighted components
        return 0.25 * tent + 0.20 * sph_harm + 0.18 * saddle + 0.15 * mixed + 0.12 * barrier + 0.10 * coupling