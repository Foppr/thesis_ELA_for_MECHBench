import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Radial basin term - encourages convergence to origin
        radial_term = np.sum(x**2) * 0.05
        
        # Sinusoidal oscillation terms with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(np.pi * (x[i] + x[j]))
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
            
        # Combine all terms with different weights
        result = radial_term + sin_term * 0.5 + cross_term * 0.3 + chaotic_term * 0.2
        
        # Add small noise for additional challenge
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + noise