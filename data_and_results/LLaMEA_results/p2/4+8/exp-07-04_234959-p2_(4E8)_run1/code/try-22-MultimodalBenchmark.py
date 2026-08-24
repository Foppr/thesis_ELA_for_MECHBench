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
        f2 = np.sum(np.sin(10.0 * x) * np.cos(3.0 * x))
        
        # Additional cosine interactions to create more complex landscape
        f3 = np.sum(np.cos(7.0 * x) * np.sin(2.0 * x))
        
        # Exponential decay terms with adaptive scaling
        f4 = np.sum(np.exp(-0.05 * x**2) * np.sin(4.0 * x))
        
        # Shifted global minimum to increase challenge
        shift = np.ones(self.dim) * 0.5
        f5 = np.sum((x - shift)**2)
        
        # Combine all terms with different weights
        return 0.15 * f1 + 0.25 * f2 + 0.20 * f3 + 0.25 * f4 + 0.15 * f5