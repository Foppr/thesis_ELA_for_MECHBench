import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_norm**2)
        
        # Highly oscillatory sinusoidal components with exponential scaling
        sinusoidal_term = np.sum(np.exp(10 * np.abs(x_norm)) * np.sin(3 * np.pi * x_norm)**2)
        
        # Polynomial mixture with varying degrees for complexity
        polynomial_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Central ruggedness term to create many local minima
        rugged_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Combine all terms with adaptive weights
        result = 0.5 * quadratic_term + 0.3 * sinusoidal_term + 0.2 * polynomial_term + 0.1 * rugged_term
        
        return result