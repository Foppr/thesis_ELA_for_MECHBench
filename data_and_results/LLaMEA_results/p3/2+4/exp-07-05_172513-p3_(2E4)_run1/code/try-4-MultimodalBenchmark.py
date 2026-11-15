import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for global convergence
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms creating dense local minima
        sinusoidal = np.sum(np.sin(10 * np.pi * x_normalized) ** 2)
        
        # Additional high-order polynomial terms for increased conditioning
        polynomial = np.sum(x_normalized**6)
        
        # Exponentially increasing penalty term to discourage large values
        penalty = np.sum(np.exp(2 * np.abs(x_normalized)) - 1)
        
        # Cross-term interaction to increase problem complexity
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:])
        
        return quadratic + 2.0 * sinusoidal + 0.5 * polynomial + penalty + 0.1 * cross_term