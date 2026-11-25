import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Sinusoidal wave component creating many local optima
        wave_term = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Polynomial penalty terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 4) + 0.5 * (x[i] ** 3) + 2.0 * (x[i] ** 2)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_term += np.sin(x[i]) * np.cos(x[i])
            else:
                chaotic_term += np.sin(x[i-1] + x[i]) * np.cos(x[i-1] - x[i])
        
        # Combine all terms with different weights
        result = wave_term + 0.5 * poly_term + 0.3 * chaotic_term
        
        # Add a small noise term to make it more challenging
        noise = 0.001 * np.sum(np.random.randn(self.dim))
        
        return result + noise