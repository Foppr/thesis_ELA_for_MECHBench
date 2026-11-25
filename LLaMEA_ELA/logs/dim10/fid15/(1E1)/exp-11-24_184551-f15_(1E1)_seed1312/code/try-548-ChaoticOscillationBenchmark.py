import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial quadratic basin term
        radial_term = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillation terms with different frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Add chaotic behavior with logistic map-like terms
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Combine all terms with different weights
        result = radial_term - sin_term + cross_term - chaotic_term
        
        # Add small random noise to make it non-trivial
        noise = 0.001 * np.sum(np.random.rand(self.dim) * x)
        
        return result + noise