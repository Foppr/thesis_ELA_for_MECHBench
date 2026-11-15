import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal terms
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.2)**2)
        
        # Add a global minimum at the origin with additional penalty terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.1 * (x_normalized[i]**4 - 2 * x_normalized[i]**2)
            
        return quadratic + sinusoidal + penalty