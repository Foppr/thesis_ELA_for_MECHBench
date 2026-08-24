import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product of cosine terms
        f3 = np.prod(np.cos(2 * np.pi * x_norm))
        
        # Additional multimodal component
        f4 = np.sum((x_norm + 0.5)**4)
        
        # Combine all components with different weights
        result = 0.5 * f1 + 0.3 * f2 + 0.1 * f3 + 0.1 * f4
        
        # Add a small noise term to make it more challenging
        noise = 0.01 * np.random.random()
        
        return result + noise