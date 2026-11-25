import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal wave components in different directions
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Polynomial penalty terms to create complex landscape
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 4) - 2.0 * (x[i] ** 2)
            
        # Chaotic interaction term between dimensions
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += np.sin(x[i] * x[j]) * 0.5
                
        # Add a global quadratic basin to encourage convergence
        basin_term = 0.1 * np.sum(x**2)
        
        # Combine all terms with different weights
        result = wave_term + poly_term + chaotic_term + basin_term
        
        return result