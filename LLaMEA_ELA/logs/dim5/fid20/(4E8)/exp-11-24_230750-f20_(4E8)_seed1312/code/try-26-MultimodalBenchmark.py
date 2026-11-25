import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with varying widths
        rbfs = np.sum(np.exp(-np.sum((x[:, None] - np.linspace(-5, 5, 10))**2, axis=0) / (2 * (0.5 + 0.5 * np.sin(self.dim))**2)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * self.dim
        
        # Asymmetric saddle points with polynomial interactions
        saddle = np.sum((x**3 - 3 * x**2) * condition_factor)
        
        # Cross-dimensional interactions with exponential decay
        cross_interaction = np.sum(np.exp(-np.abs(x[:-1] - x[1:]) / (1 + self.dim * 0.1)))
        
        # Combined function value
        return rbfs + saddle + cross_interaction