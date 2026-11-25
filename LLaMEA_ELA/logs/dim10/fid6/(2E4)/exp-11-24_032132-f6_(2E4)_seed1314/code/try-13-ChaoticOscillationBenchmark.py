import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1, 1, dim)
        self.frequency = np.random.uniform(1, 5, dim)
        self.exponent = np.random.uniform(2, 4, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial basin term
        basin = np.sum(self.coefficients * (x ** self.exponent))
        
        # Sinusoidal oscillation terms
        oscillation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillation += np.sin(self.frequency[i] * x[i]) * np.cos(self.frequency[j] * x[j])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x[i]**2) * np.tan(x[i])
            
        # Combine all components with dynamic weighting
        result = basin + 0.5 * oscillation + 0.3 * chaotic
        
        # Add small noise to prevent exact replication
        return result + np.random.normal(0, 0.001)