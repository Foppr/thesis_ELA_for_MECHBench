import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1 + 0.5 * np.sin(3 * r))
        
        # Angular components with multiple frequencies
        angles = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0.0
        angular = np.sum(np.cos((np.arange(1, self.dim + 1) + 1) * angles)) if self.dim > 1 else 0.0
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                chaotic += np.sin(10 * x_norm[i] + i * 0.5) * np.cos(7 * x_norm[(i+1) % self.dim])
        
        # Combine components with different weights
        return 2.0 * radial + 0.5 * angular + 0.3 * chaotic + 1.0