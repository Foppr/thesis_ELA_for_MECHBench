import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Radial basin term - pulls solutions towards origin
        radial_term = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillations creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating interaction between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + abs(x[i] - x[j]))
                
        # Additional chaotic component with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-0.1 * x[i]**2) * np.sin(2.0 * np.pi * x[i])
            
        # Combine all terms with different weights
        result = radial_term + 2.0 * sin_term + 0.5 * cross_term + 0.3 * chaotic_term
        
        return result