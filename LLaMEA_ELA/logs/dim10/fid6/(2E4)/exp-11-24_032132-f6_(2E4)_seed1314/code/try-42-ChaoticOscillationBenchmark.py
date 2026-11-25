import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1, 1, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Polynomial basin term
        basin = 0.5 * np.sum(x**4)
        
        # Sinusoidal oscillation terms
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(self.coefficients[i] * x[i]) * np.cos(2 * x[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (x[i]**2 - 1.5) * np.sin(x[i]) * np.exp(-abs(x[i]))
            
        # Combine all terms with different weights
        result = basin + 0.3 * oscillation + 0.2 * chaotic
        
        # Add small noise for non-triviality
        result += np.random.normal(0, 0.001)
        
        return result