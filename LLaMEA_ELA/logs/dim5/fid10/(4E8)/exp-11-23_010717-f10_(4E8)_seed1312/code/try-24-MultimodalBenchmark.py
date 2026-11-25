import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay terms that create rugged landscape
        exp_terms = np.sum(np.exp(-x_normalized**2) * np.cos(10 * np.pi * x_normalized))
        
        # High-frequency trigonometric components for multiple local minima
        trig_terms = np.sum(np.sin(20 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Quadratic basin term to ensure global minimum at origin
        quadratic_term = 0.5 * np.sum(x_normalized**2)
        
        # Additional penalty for large values to increase complexity
        penalty = 0.1 * np.sum(np.abs(x_normalized)**3)
        
        # Combine all components
        return exp_terms + trig_terms + quadratic_term + penalty