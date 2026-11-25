import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_normalized[i]) * np.exp(-0.1 * (x_normalized[i] - 0.5)**2)
        
        # Add a polynomial term to increase complexity
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x_normalized[i]**4
        
        return quadratic_term + 0.1 * sin_term + 0.01 * poly_term