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
        f2 = np.sum(np.sin(20.0 * x) * np.cos(7.0 * x))
        
        # Additional cosine interactions to create more complex landscape
        f3 = np.sum(np.cos(12.0 * x) * np.sin(4.0 * x))
        
        # Exponential decay terms with adaptive scaling
        f4 = np.sum(np.exp(-0.15 * x**2) * np.sin(8.0 * x))
        
        # Cubic polynomial interactions to increase complexity
        f5 = np.sum(x**3 * np.sin(3.0 * x))
        
        # Shifted global minimum to increase challenge
        shift = np.ones(self.dim) * 1.5
        f6 = np.sum((x - shift)**2)
        
        # Combine all terms with different weights
        return 0.12 * f1 + 0.18 * f2 + 0.17 * f3 + 0.23 * f4 + 0.16 * f5 + 0.14 * f6