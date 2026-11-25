import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Add a small noise term to create a more complex landscape
        noise_term = 0.1 * np.random.random()
        
        # Combine terms to create multimodal landscape
        result = quadratic_term + 0.1 * sinusoidal_term + noise_term
        
        return result