import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal oscillations with exponential growth
        f2 = np.sum(np.sin(10.0 * np.exp(0.5 * np.abs(x)) * x))
        
        # Polynomial corruption with varying degrees
        f3 = 0.01 * np.sum(x**6 + 0.5 * x**5 + 0.2 * x**4)
        
        # Add saddle point structure
        f4 = 0.1 * np.sum(np.cos(2.0 * x) * np.sin(0.5 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4