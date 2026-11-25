import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - encourages convergence to origin
        radial_basin = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation terms - create chaotic landscape
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + abs(x[i] - x[j]))
                
        # Additional chaotic component with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-0.5 * x[i]**2) * np.sin(10.0 * x[i])
            
        # Combine all terms with different weights
        result = radial_basin + 2.0 * sin_term + 0.5 * cross_term + 0.3 * chaotic_term
        
        return result