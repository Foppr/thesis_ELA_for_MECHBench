import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms to create steep gradients near boundaries
        barrier = np.sum(-np.log(25.0 - x**2))
        
        # High-frequency trigonometric oscillations with exponential decay
        oscillations = np.sum(np.exp(-x**2 / 10.0) * np.sin(10 * x) * np.cos(15 * x))
        
        # Polynomial conditioning with cross-dimensional interactions
        polynomial = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Cross-dimensional interaction terms
        cross_dim = np.sum((x[:-1] - x[1:])**2 * np.exp(-np.abs(x[:-1] - x[1:]) / 5.0))
        
        result = barrier + oscillations + polynomial + cross_dim
        
        return result