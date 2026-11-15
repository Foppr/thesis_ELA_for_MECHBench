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
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm)**2 + 0.5 * np.sin(10 * np.pi * x_norm)**2)
        
        # High-order polynomial terms for increased complexity
        polynomial = np.sum(x_norm**4 + 0.3 * x_norm**6)
        
        # Product of all dimensions (creates correlations)
        product = np.prod(x_norm)
        
        # Additional periodic interaction terms with varying weights
        interaction = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) + 
                            0.5 * np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Cross-terms that create more complex interactions between dimensions
        cross_terms = np.sum((x_norm[:-1] - x_norm[1:])**2 * np.sin(5 * np.pi * x_norm[:-1])**2)
        
        # Add a small noise term to make it non-trivial
        noise = 0.05 * np.random.random()
        
        # Combine all terms with different weights
        return 0.4 * quadratic + 0.3 * sinusoidal + 0.2 * polynomial + 0.1 * product + 0.1 * interaction + 0.05 * cross_terms + noise