import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with exponential growth
        f2 = 0.3 * np.sum(np.sin(8.0 * x) * np.exp(-0.2 * x**2) * (1 + 0.5 * np.abs(x)))
        
        # Cross-terms creating complex interaction between dimensions
        f3 = 0.1 * np.sum(np.sin(x[:-1] + x[1:]) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)) * (1 + 0.3 * np.abs(x[:-1] + x[1:])))
        
        # Chaotic component using a modified logistic map for high complexity
        chaotic = 0.05 * np.sum(np.sin(10.0 * np.abs(x) * np.sin(2.0 * np.pi * x)) * np.exp(-0.15 * x**2))
        
        # Add a fractional power term to increase non-linearity
        f4 = 0.01 * np.sum(np.abs(x)**1.7)
        
        # Add a periodic modulation with varying frequency
        f5 = 0.2 * np.sum(np.cos(15.0 * x) * np.exp(-0.05 * x**2) * (1 + 0.4 * np.sin(3.0 * x)))
        
        return f1 + f2 + f3 + chaotic + f4 + f5