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
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x))
        
        # Polynomial corruption with varying degrees
        f3 = 0.015 * np.sum(x**7 + 0.5 * x**6 + 0.2 * x**5 + 0.05 * x**4)
        
        # Add saddle point structure with stronger interaction
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Introduce additional chaotic component for increased complexity
        f5 = 0.07 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        # Add a new term to enhance global optima distinctiveness
        f6 = 0.1 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6