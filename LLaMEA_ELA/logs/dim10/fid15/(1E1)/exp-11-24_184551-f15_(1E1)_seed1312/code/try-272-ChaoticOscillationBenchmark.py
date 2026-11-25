import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Base polynomial basin term
        basin = 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillation terms with varying frequencies
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(np.pi * (x[i] + x[j]))
                
        # Additional chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * x[i]) * np.cos(5 * np.pi * x[i])
            
        # Combine all terms with different weights
        result = basin + 0.5 * oscillation + 0.3 * cross_term + 0.2 * chaotic
        
        # Add small noise for non-triviality
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + noise