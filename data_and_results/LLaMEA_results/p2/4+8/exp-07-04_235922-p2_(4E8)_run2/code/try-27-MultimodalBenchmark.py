import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        f1 = np.sum(x**2)
        
        # Sinusoidal interference with exponentially decaying amplitude
        f2 = np.sum(np.sin(x) * np.exp(-0.1 * np.abs(x)))
        
        # Additional high-frequency oscillation with varying decay
        f3 = np.sum(np.sin(10.0 * x) * np.exp(-0.05 * x**2))
        
        # Interaction terms between dimensions
        f4 = 0.1 * np.sum((x[:-1] - x[1:])**2)
        
        return f1 + f2 + f3 + f4