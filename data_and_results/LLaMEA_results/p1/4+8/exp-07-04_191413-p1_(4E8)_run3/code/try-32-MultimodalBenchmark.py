import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Spherical symmetry term with logarithmic barrier
        r = np.sqrt(np.sum(x_scaled**2))
        spherical = r**2 * np.exp(-r**2 / 2.0)
        
        # Polynomial oscillations with chaotic behavior
        poly_osc = np.sum((x_scaled**3 - 3*x_scaled)**2)
        
        # Logarithmic barrier terms to create complex terrain
        log_barrier = np.sum(np.log(1.0 + 0.1 * x_scaled**2))
        
        # Cross-dimensional interaction with chaotic sine components
        cross_interaction = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return spherical + 0.3 * poly_osc + 0.2 * log_barrier + 0.5 * cross_interaction