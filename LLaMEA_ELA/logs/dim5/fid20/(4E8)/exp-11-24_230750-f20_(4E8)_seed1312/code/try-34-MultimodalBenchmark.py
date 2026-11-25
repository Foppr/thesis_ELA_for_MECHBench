import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms to create sharp gradients near boundaries
        barrier = np.sum(np.log(25.0 - x**2))
        
        # Complex cosine product interactions with varying frequencies
        cos_product = np.sum(np.cos(1.0 * x) * np.cos(2.0 * x) * np.cos(3.0 * x) * np.cos(4.0 * x))
        
        # Saddle-point inducing polynomial terms with alternating signs
        saddle_terms = np.sum(x**6 - 15.0 * x**4 + 75.0 * x**2 - 125.0)
        
        # Chaotic sine modulation with dynamic frequency scaling
        chaotic_mod = np.sum(np.sin(10.0 * np.sin(x)) * np.cos(5.0 * np.cos(x)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Combined function value
        return barrier + cos_product + saddle_terms + chaotic_mod + cross_coupling