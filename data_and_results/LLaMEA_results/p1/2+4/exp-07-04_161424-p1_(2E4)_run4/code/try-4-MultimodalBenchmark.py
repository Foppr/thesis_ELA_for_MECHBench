import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic term for conditioning and global minimum
        quadratic = np.sum(x_norm**2)
        
        # Highly oscillatory sinusoidal terms with exponential growth
        oscillatory = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(2 * np.abs(x_norm)))
        
        # Non-separable interaction term using exponential decay
        interaction = np.exp(-np.sum(x_norm**2) / (2 * self.dim))
        
        # Add saddle point structure with polynomial terms
        saddle = np.sum(x_norm**4) - 0.5 * np.sum(x_norm**2)
        
        # Combine all components with varying weights
        return 0.5 * quadratic + 2.0 * oscillatory + 0.1 * interaction + 0.3 * saddle