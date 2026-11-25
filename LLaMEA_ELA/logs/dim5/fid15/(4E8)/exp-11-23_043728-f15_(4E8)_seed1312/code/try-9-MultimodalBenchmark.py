import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic_term = np.sum(x_norm**2)
        
        # Multiple sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm)) + \
                   np.sum(np.sin(7 * np.pi * x_norm)**2) + \
                   0.5 * np.sum(np.sin(15 * np.pi * x_norm)**3)
        
        # Clustered local minima using radial basis functions
        cluster_term = 0.0
        centers = np.array([[-0.5, 0.5], [0.5, -0.5], [-0.3, -0.7], [0.8, 0.2]])
        for center in centers:
            if self.dim >= 2:
                dist = np.sum((x_norm[:2] - center)**2)
                cluster_term += np.exp(-dist * 10) * np.sin(dist * 5)
        
        # High-order polynomial terms for increased complexity
        poly_term = np.sum(x_norm**8) + 0.1 * np.sum(x_norm**10) + 0.01 * np.sum(np.abs(x_norm)**12)
        
        # Additional coupling terms between dimensions
        coupling_term = 0.0
        for i in range(0, self.dim - 1):
            coupling_term += (x_norm[i] - x_norm[i+1])**4
        
        # Combine all terms with different weights to create a challenging landscape
        return quadratic_term + 0.8 * sin_term + 0.02 * poly_term + 0.5 * cluster_term + 0.3 * coupling_term