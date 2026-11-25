import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - encourages convergence to origin
        radial_term = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Chaotic component with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-np.abs(x[i])) * np.sin(np.pi * x[i])
            
        # Combine all terms with different weights
        return radial_term + 0.5 * sin_term + 0.3 * cross_term + 0.2 * chaotic_term