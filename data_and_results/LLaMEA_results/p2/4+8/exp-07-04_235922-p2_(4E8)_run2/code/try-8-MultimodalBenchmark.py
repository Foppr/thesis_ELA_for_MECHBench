import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with higher frequency to create more local minima
        sinusoidal = np.sum(np.sin(7 * np.pi * x_normalized)**2)
        
        # Product term with modified cosine to create complex landscape
        product = np.prod(np.cos(3 * np.pi * x_normalized) + 1.5)
        
        # Additional polynomial interaction term
        polynomial_interaction = np.sum(x_normalized**4)
        
        # Combine terms with different weights
        return 0.1 * quadratic + 0.4 * sinusoidal + 0.4 * product + 0.1 * polynomial_interaction