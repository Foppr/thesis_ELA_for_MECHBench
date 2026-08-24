import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies and interactions
        sinusoidal = np.sum(np.sin(3 * np.pi * x_norm) ** 2) + 0.5 * np.sum(np.sin(7 * np.pi * x_norm) ** 2)
        
        # Add cross-terms to increase landscape complexity
        cross_terms = 0.3 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Add a small noise term to create more complex landscape
        noise = 0.05 * np.random.random()
        
        # Combine terms to create multimodal landscape
        return quadratic + sinusoidal + cross_terms + noise