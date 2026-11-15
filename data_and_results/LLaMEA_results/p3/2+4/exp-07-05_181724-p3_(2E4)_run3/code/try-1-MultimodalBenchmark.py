import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product of all dimensions (creates correlations)
        product = np.prod(x_norm)
        
        # Add a small noise term to make it non-trivial
        noise = 0.1 * np.random.random()
        
        return quadratic + 0.5 * sinusoidal + 0.1 * product + noise