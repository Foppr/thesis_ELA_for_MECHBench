import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(20 * np.pi * x_norm) * np.sin(15 * np.pi * x_norm))
        
        # Radial basis function component with dynamic conditioning
        f3 = 0.3 * np.sum(np.exp(-5 * x_norm**2) * np.cos(10 * np.pi * x_norm))
        
        # Higher-order polynomial terms for increased complexity
        f4 = 0.05 * np.sum(x_norm**4)
        f5 = 0.02 * np.sum(x_norm**6)
        f6 = 0.01 * np.sum(x_norm**8)
        
        # Cross-dimensional interaction terms with chaotic modulation
        f7 = 0.04 * np.sum(np.sin(8 * np.pi * x_norm[:-1]) * x_norm[1:])
        f8 = 0.03 * np.sum(np.cos(12 * np.pi * x_norm[:-2]) * x_norm[2:])
        
        # Dynamic conditioning based on dimension
        condition_factors = np.array([np.sin(np.pi * (i + 1) / self.dim) for i in range(self.dim)])
        f9 = 0.02 * np.sum(x_norm**2 * condition_factors)
        
        # Additional chaotic modulation with exponential decay
        f10 = 0.1 * np.sum(np.exp(-3 * np.abs(x_norm)) * np.sin(25 * np.pi * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10