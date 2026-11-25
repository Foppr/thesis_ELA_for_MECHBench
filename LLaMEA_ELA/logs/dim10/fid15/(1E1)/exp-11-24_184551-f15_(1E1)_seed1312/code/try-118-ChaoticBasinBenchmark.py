import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - encourages convergence to origin
        radial_basin = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation terms - create many local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Chaotic component with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-np.abs(x[i])) * np.cos(10.0 * x[i])
            
        # Combine all terms with different weights
        result = radial_basin + sin_term + cross_term + chaotic_term
        
        return result