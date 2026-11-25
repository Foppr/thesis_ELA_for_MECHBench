import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1 + 0.5 * np.sin(10 * r))
        
        # Angular components with multiple frequencies
        angular = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x_norm[j], x_norm[i])
                angular += np.cos((i+1) * (j+1) * angle) * np.sin(3 * angle)
        
        # Add chaotic sine wave component
        chaotic = np.sum(np.sin(7 * x_norm + np.sin(5 * x_norm))**2)
        
        # Combine components with different weights
        return 0.5 * radial + 0.3 * angular + 0.2 * chaotic