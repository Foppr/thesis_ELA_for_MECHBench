import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial growth term creating broad basins
        poly_term = np.sum(x_scaled**4)
        
        # Sinusoidal modulation with varying frequencies
        sin_modulation = np.sum(np.sin(2.0 * np.pi * x_scaled) * np.cos(3.0 * np.pi * x_scaled))
        
        # Logarithmic barrier terms near boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.log(1.0 + 10.0 * (1.0 - abs(x_scaled[i]))**2)
        
        # Chaotic saddle point component using tent map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            chaotic += (4.0 * xi * (1.0 - xi)) if xi < 0.5 else (4.0 * (1.0 - xi) * xi)
        
        # Combine all components with different weights
        result = 0.5 * poly_term + 0.3 * sin_modulation + 0.2 * barrier + 0.1 * chaotic
        
        return result