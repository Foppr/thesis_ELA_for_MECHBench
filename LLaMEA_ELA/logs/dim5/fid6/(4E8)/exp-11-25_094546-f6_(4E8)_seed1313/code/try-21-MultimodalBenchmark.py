import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2)
        
        # Angular components with multiple frequencies
        angles = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0.0
        angular = np.sin(5 * angles) + 0.5 * np.cos(12 * angles)
        
        # Multi-scale sinusoidal modulation
        modulated = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Clustered minima with varying distances from origin
        cluster_term = 0.0
        for i in range(self.dim):
            cluster_term += (x_norm[i] - np.sin(i))**2 + (x_norm[i] - np.cos(i))**2
            
        # Combine all components with different weights
        return 10 * radial + 2 * angular + 0.5 * modulated + 0.1 * cluster_term