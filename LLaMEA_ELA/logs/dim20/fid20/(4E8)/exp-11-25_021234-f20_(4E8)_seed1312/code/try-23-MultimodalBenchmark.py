import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Add multiple sinusoidal modulations with different frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(3.0 * x) * np.sin(7.0 * x) * np.exp(-0.1 * x**2))
        
        # Add a periodic component that creates a grid-like structure of local minima
        f3 = 0.3 * np.sum(np.cos(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.05 * x**2))
        
        # Add a fourth term to create more complex interactions between dimensions
        f4 = 0.2 * np.sum(np.sin(6.0 * x) * np.cos(3.0 * x) * np.exp(-0.15 * x**2))
        
        return f1 + f2 + f3 + f4