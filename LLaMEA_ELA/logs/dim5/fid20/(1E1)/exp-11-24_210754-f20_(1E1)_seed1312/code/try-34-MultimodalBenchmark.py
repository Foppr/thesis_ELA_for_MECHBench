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
        f2 = np.sum(np.sin(15.0 * np.exp(0.7 * np.abs(x)) * x))
        
        # Polynomial corruption with varying degrees
        f3 = 0.01 * np.sum(x**7 + 0.6 * x**6 + 0.3 * x**5 + 0.1 * x**4)
        
        # Add saddle point structure with stronger interaction
        f4 = 0.15 * np.sum(np.cos(3.0 * x) * np.sin(0.7 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Introduce additional chaotic component for increased complexity
        f5 = 0.05 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        # Add a new chaotic modulation with shifted exponential decay
        f6 = 0.1 * np.sum(np.sin(20.0 * x) * np.exp(-0.5 * (x - 1.0)**2))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6