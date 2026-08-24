import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal terms with varying amplitudes
        f2 = np.sum(np.sin(25.0 * x) * np.cos(8.0 * x))
        
        # Additional cosine interactions to create more complex landscape
        f3 = np.sum(np.cos(15.0 * x) * np.sin(5.0 * x))
        
        # Exponential decay terms with adaptive scaling
        f4 = np.sum(np.exp(-0.2 * x**2) * np.sin(10.0 * x))
        
        # Higher-order polynomial interactions to increase complexity
        f5 = np.sum(x**4 * np.sin(3.0 * x))
        
        # Multiple exponential barrier terms to create rugged landscape
        f6 = np.sum(np.exp(-0.5 * (x - 2.0)**2) + np.exp(-0.5 * (x + 2.0)**2))
        
        # Additional cubic polynomial interactions
        f7 = np.sum(x**3 * np.cos(4.0 * x))
        
        # Shifted global minimum to increase challenge
        shift = np.ones(self.dim) * 1.5
        f8 = np.sum((x - shift)**2)
        
        # Combine all terms with different weights
        return 0.05 * f1 + 0.25 * f2 + 0.15 * f3 + 0.20 * f4 + 0.10 * f5 + 0.10 * f6 + 0.10 * f7 + 0.05 * f8