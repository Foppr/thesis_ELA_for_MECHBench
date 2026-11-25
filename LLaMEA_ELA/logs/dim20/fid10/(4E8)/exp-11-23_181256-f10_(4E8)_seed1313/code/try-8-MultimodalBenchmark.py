import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Quadratic term with varying coefficients
        quadratic_term = np.sum((x_norm ** 2) * (np.arange(1, self.dim + 1) / self.dim))
        
        # Sinusoidal terms with exponentially increasing frequencies
        freqs = np.exp(np.arange(1, self.dim + 1) * 0.5)
        sinusoidal_term = np.sum(np.sin(freqs * x_norm) ** 2)
        
        # Polynomial term with high degree for increased complexity
        polynomial_term = np.sum((x_norm ** 7) * (np.arange(1, self.dim + 1) / self.dim))
        
        # Interaction term creating complex landscape
        interaction_term = np.prod(np.sin(0.3 * np.pi * x_norm) * np.cos(0.7 * np.pi * x_norm))
        
        # Combine all terms with different weights
        return 0.5 * quadratic_term + 0.3 * sinusoidal_term + 0.2 * polynomial_term - 0.1 * interaction_term