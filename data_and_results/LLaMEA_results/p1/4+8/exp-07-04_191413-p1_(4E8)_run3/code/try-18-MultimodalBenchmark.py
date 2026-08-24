import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial term with polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        
        # Polynomial oscillation in radial direction
        radial_osc = np.sin(10 * r) * np.cos(5 * r)
        
        # Sum of sinusoidal terms in each dimension
        dim_osc = np.sum(np.sin(3 * np.pi * x_norm) ** 2)
        
        # Exponential barrier near the boundary
        barrier = np.sum(np.exp(-10 * (1 - np.abs(x_norm))**2))
        
        # Combine terms with different weights
        return r**4 + 0.5 * radial_osc + 0.3 * dim_osc + 0.1 * barrier