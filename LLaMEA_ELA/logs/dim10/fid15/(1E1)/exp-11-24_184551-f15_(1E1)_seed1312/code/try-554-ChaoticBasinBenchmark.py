import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1.0, 1.0, size=dim)
        self.frequency = np.random.uniform(0.5, 2.0, size=dim)
        self.power_exponents = np.random.uniform(1.5, 4.0, size=dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial basin term
        basin = np.sum(np.power(np.abs(x), self.power_exponents)) * 0.01
        
        # Sinusoidal modulation term
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(self.frequency[i] * x[i]) * np.cos(self.coefficients[i] * x[i])
        
        # Chaotic component with exponential scaling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-np.abs(x[i])) * np.sin(10 * x[i]**2)
            
        # Add noise and interaction terms
        noise = np.sum(np.random.uniform(-0.01, 0.01, self.dim))
        interaction = np.sum(x[:-1] * x[1:]) * 0.001
        
        return basin - sin_term + chaotic + noise + interaction