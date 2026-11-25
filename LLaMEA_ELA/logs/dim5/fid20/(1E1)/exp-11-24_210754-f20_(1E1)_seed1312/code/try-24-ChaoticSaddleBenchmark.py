import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic component using sine and cosine with varying frequencies
        f2 = np.sum(np.sin(10.0 * np.sin(x)) * np.cos(7.0 * np.cos(x)))
        
        # Nested saddle points with logarithmic modulation
        f3 = 0.5 * np.sum((x**2 - 1)**2 * np.log(np.abs(x) + 1e-8))
        
        # High-frequency oscillation with exponential decay
        f4 = np.sum(np.sin(20.0 * np.exp(-0.5 * np.abs(x)) * x) * np.exp(-0.1 * x**2))
        
        # Asymmetric polynomial corruption with mixed degrees
        f5 = 0.3 * np.sum(np.sign(x) * (np.abs(x)**3 + 0.5 * np.abs(x)**2.5 + 0.1 * np.abs(x)**1.7))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5