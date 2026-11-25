import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x**4) / 4.0
        
        # Trigonometric terms creating multiple local minima
        f2 = np.sum(np.sin(3.0 * x)**2)
        
        # Exponential decay terms for varied curvature
        f3 = np.sum(np.exp(-0.5 * x**2))
        
        # Cross-terms to increase dimensionality interaction
        f4 = 0.1 * np.sum(x[:-1]**2 * x[1:]**2)
        
        # Sine modulation with varying frequencies
        f5 = 0.05 * np.sum(np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5