import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with exponential modulation
        for i in range(self.dim):
            xi = x[i]
            # Sinusoidal component with varying frequency
            sin_term = np.sin(5 * xi) * np.cos(3 * xi)
            # Exponential barrier to create steep gradients
            exp_barrier = np.exp(-0.1 * xi**2)
            # Polynomial modulation
            poly_mod = 1 + 0.1 * xi**4
            result += sin_term * exp_barrier * poly_mod
            
        # Add global quadratic term for conditioning
        quad_term = 0.01 * np.sum(x**2)
        
        # Add noise-like component to increase complexity
        noise = 0.05 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return result + quad_term + noise + 10 * self.dim