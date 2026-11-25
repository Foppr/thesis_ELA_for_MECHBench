import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.3)**2) + \
                       np.sin(7 * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] + 0.4)**2)
        
        # Add a polynomial term to increase complexity with mixed exponents
        poly_term = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                poly_term += x_normalized[i]**6
            else:
                poly_term += x_normalized[i]**3
        
        # Add interaction terms between dimensions to increase problem complexity
        interaction_term = 0.0
        for i in range(self.dim-1):
            interaction_term += (x_normalized[i] - x_normalized[i+1])**2 * np.exp(-0.1 * (x_normalized[i] + x_normalized[i+1])**2)
        
        return quadratic_term + 0.15 * sin_term + 0.02 * poly_term + 0.05 * interaction_term