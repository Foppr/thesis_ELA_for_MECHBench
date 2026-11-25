import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial terms with varying degrees to create diverse curvature
        poly_term = np.sum(x_normalized**4 + 0.5 * x_normalized**3 + 0.1 * x_normalized**2)
        
        # Sinusoidal modulation with multiple frequencies to introduce local minima
        sin_term = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Exponential decay term to create shallow regions near the origin
        exp_term = np.sum(np.exp(-x_normalized**2 / 2.0) - 1.0)
        
        # Additional coupling term between dimensions to increase complexity
        coupling_term = 0.3 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Combine all terms
        return poly_term + sin_term + exp_term + coupling_term