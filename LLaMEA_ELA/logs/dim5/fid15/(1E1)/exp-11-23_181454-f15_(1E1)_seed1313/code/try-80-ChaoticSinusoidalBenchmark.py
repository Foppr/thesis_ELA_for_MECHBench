import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Global minimum at origin
        result = 0.0
        
        # Add exponentially decaying sinusoidal components
        for i in range(self.dim):
            # Use each dimension with different frequency and decay rate
            freq = 2 * np.pi * (i + 1)
            decay = np.exp(-0.1 * i)
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add quadratic term to create a basin around the minimum
        result += 0.01 * np.sum(x**2)
        
        # Add a chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic_term += np.sin(10 * x[i-1] * x[i])
        
        result += 0.05 * chaotic_term
        
        # Add a small noise term to increase challenge
        result += 0.001 * np.sum(np.random.randn(self.dim) * x)
        
        return result