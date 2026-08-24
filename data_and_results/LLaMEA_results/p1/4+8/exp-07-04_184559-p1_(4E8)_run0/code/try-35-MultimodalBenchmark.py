import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine modulation with varying frequencies
        f2 = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.5 * np.sin(3 * np.pi * x_norm)))**2)
        
        # Radial bias term with exponential barrier
        r = np.sqrt(np.sum(x_norm**2))
        f3 = 0.5 * np.exp(2 * r) * np.sin(5 * np.pi * r)**2
        
        # Additional high-frequency sinusoidal term
        f4 = 0.3 * np.sum(np.sin(20 * np.pi * x_norm)**4)
        
        # Combine all terms
        return f1 + 0.8 * f2 + 0.2 * f3 + 0.4 * f4