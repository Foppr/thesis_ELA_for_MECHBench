import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal oscillations with exponential growth and cross-dimensional interaction
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x * np.sin(0.5 * x)))
        
        # Polynomial corruption with varying degrees and cross-terms
        f3 = 0.01 * np.sum(x**7 + 0.6 * x**6 + 0.3 * x**5 + 0.1 * x**4 + 0.05 * np.prod(x.reshape(-1, 1), axis=0))
        
        # Add saddle point structure with stronger interaction and chaotic modulation
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)) * np.sin(0.3 * np.sum(x**2)))
        
        # Introduce additional chaotic component with enhanced nonlinearity
        f5 = 0.08 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(0.1 * x))
        
        # Add cross-dimensional interaction terms for increased complexity
        f6 = 0.03 * np.sum((x[:-1] - x[1:])**2 * np.sin(10.0 * x[:-1]))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6