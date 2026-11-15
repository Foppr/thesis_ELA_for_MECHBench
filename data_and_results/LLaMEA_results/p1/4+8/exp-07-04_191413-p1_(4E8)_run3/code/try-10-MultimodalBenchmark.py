import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial term that penalizes distance from origin
        radial = np.sum(x_norm**2)
        
        # Radially symmetric oscillations with exponential decay
        r = np.sqrt(radial)
        oscillation = np.sum(np.exp(-10 * r) * np.sin(20 * np.pi * r) ** 2)
        
        # Cross-terms creating complex interaction between dimensions
        cross = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(10 * np.pi * x_norm[:-1]) ** 2)
        
        # Combine terms with different weights
        return 0.5 * radial + 0.3 * oscillation + 0.2 * cross