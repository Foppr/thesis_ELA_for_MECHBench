import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple local minima
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Additional penalty term to create complex landscape
        penalty_term = 0.1 * np.sum(np.abs(x_normalized))
        
        # Combine all terms to create a challenging optimization landscape
        return quadratic_term + sinusoidal_term + penalty_term