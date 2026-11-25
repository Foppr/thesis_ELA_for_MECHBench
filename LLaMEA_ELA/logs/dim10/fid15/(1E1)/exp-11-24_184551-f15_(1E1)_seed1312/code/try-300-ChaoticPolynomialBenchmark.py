import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial potential terms
        polynomial_term = 0.0
        for i in range(self.dim):
            polynomial_term += x[i]**4 - 2*x[i]**2 + 0.5*x[i]
        
        # Sinusoidal chaotic component
        sinusoidal_term = 0.0
        for i in range(self.dim):
            sinusoidal_term += np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Cross-term interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * (i + j)
        
        # Add noise and scaling
        noise = np.random.normal(0, 0.01)
        return polynomial_term + sinusoidal_term + cross_term + noise