import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic sine wave perturbations with varying frequencies
        f2 = np.sum(np.sin(15.0 * x + np.sin(5.0 * x)) * np.exp(-0.3 * np.abs(x)))
        
        # Gaussian peaks with random positions and heights
        f3 = 0.0
        for i in range(self.dim):
            f3 -= 2.0 * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(i))**2 + (x[i] - 3.0 * np.cos(i))**2))
        
        # Long-range interaction term with fractal-like behavior
        f4 = 0.2 * np.sum(np.sin(0.1 * x) * np.cos(0.05 * np.sum(x)) * np.exp(-0.1 * np.sum(x**2)))
        
        # Additional non-convex penalty with multiple local minima
        f5 = 0.1 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Add a complex global minimum structure
        f6 = 0.05 * np.sum(np.abs(x)**3.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6