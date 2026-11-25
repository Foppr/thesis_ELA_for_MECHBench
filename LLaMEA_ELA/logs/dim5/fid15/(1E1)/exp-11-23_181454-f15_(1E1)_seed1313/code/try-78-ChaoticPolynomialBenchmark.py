import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Sinusoidal wave component creating irregular landscape
        wave_term = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Polynomial penalty terms to create multiple local minima
        poly_term = np.sum(x**4 - 10 * x**2 + 5 * x)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += (x[i]**2 + x[i+1]**2) * np.sin(100 * x[i] * x[i+1])
        
        # Add noise to increase challenge
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x)
        
        return wave_term + poly_term + chaotic_term + noise