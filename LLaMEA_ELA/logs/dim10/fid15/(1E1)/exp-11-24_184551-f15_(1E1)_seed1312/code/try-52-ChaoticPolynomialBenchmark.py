import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial potential term
        poly_term = np.sum(x**4) * 0.01
        
        # Sinusoidal chaotic component
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * 0.1
                
        # Add a small random component to increase chaos
        random_term = np.sum(np.random.uniform(-0.01, 0.01, self.dim))
        
        return poly_term - sin_term + cross_term + random_term