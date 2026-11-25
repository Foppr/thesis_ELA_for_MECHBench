import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial basin term
        basin = 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillation terms
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-term interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (x[i] * x[j]) / (1.0 + abs(x[i] - x[j]))
                
        # Chaotic component with exponential scaling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-abs(x[i])) * np.sin(10.0 * x[i])
            
        # Combine all terms
        return basin + oscillation + cross + chaotic