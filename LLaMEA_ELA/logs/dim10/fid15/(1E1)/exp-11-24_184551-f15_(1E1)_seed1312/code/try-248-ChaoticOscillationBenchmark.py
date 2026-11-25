import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial potential term
        polynomial_term = np.sum(x**4) * 0.01
        
        # Sinusoidal oscillation term with varying frequencies
        sinusoidal_term = 0.0
        for i in range(self.dim):
            sinusoidal_term += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_term += x[i]**2 * np.sin(10 * np.pi * x[i])
            else:
                chaotic_term += x[i] * np.sin(5 * np.pi * x[i-1]) * np.cos(7 * np.pi * x[i])
        
        # Add coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += (x[i] - x[i+1])**2 * 0.1
            
        # Combine all terms with different weights
        result = polynomial_term + sinusoidal_term + chaotic_term + coupling_term
        
        # Add small noise to prevent trivial solutions
        noise = np.random.normal(0, 0.001)
        
        return result + noise