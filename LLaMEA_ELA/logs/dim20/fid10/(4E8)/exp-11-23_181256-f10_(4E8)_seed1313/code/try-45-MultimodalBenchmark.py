import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees to create different curvature
        poly_term = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**4 + 0.1 * x_norm**2)
        
        # Logarithmic barrier terms to create sharp gradients near boundaries
        log_barrier = np.sum(-np.log(1.0 - x_norm**2 + 1e-10))
        
        # Chaotic sine-wave interaction between dimensions
        sine_interaction = 0.0
        for i in range(self.dim - 1):
            sine_interaction += np.sin(10 * np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(7 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Coupling terms with exponential decay to create complex dependency
        coupling_term = np.sum(np.exp(-5.0 * np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Combine all terms with different weights to create a challenging landscape
        return 0.4 * poly_term + 0.3 * log_barrier + 0.2 * sine_interaction + 0.1 * coupling_term