import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Exponential decay terms with varying rates to create complex valleys
        f2 = 0.3 * np.sum(np.exp(-2.0 * np.abs(x_normalized)) * np.sin(5 * np.pi * x_normalized)**2)
        
        # Trigonometric interference with multiple frequencies
        f3 = 0.25 * np.sum(np.cos(3 * np.pi * x_normalized) * np.sin(6 * np.pi * x_normalized)**3)
        
        # Additional ridge-like structure with polynomial interaction
        f4 = 0.15 * np.sum((x_normalized**2 + 0.1 * np.sin(10 * np.pi * x_normalized))**2)
        
        # Combine all terms to create a challenging landscape
        return f1 + f2 + f3 + f4