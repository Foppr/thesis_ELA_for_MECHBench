import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Add a small noise term to create more complex landscape
        noise = 0.1 * np.random.random()
        
        # Combine terms to create multimodal landscape
        return quadratic + 0.5 * sinusoidal + noise