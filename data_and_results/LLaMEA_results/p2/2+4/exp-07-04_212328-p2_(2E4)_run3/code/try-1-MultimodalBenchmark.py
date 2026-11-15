import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal terms
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.1)**2)
        
        # Add a cubic term to create more complex landscape
        cubic = np.sum(x_norm**3)
        
        # Combine terms with different weights
        return 10 * quadratic + 5 * sinusoidal + 0.1 * cubic + 100 * np.exp(-0.5 * np.sum(x_norm**2))