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
        
        # Exponential decay term with radial penalty
        f4 = np.sum(np.exp(-0.05 * x**2) * (1.0 + 0.1 * np.sum(x**2)))
        
        # Shifted global minimum to increase challenge
        shift = np.ones(self.dim) * 0.5
        f5 = np.sum((x - shift)**2)
        
        # Combine all terms with carefully chosen weights
        return 0.1 * f1 + 0.2 * f2 + 0.15 * f3 + 0.3 * f4 + 0.25 * f5