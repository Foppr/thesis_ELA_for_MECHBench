import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(20 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Polynomial coupling terms to create complex interactions
        f3 = 0.15 * np.sum(x_norm**6 + x_norm**5 + x_norm**4)
        
        # Exponential decay terms to create steep gradients
        f4 = 0.2 * np.sum(np.exp(-5 * np.abs(x_norm)) * np.cos(10 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms with non-linear coupling
        f5 = 0.1 * np.sum((x_norm[:-1] + x_norm[1:]) ** 2 * np.sin(5 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Additional high-frequency oscillation for increased complexity
        f6 = 0.25 * np.sum(np.sin(30 * np.pi * x_norm**3))
        
        # Modified Gaussian-like terms with varying centers and widths
        f7 = 0.1 * np.sum(np.exp(-2 * (x_norm - 0.3)**2) + np.exp(-2 * (x_norm + 0.3)**2))
        
        # Higher-order cross-terms for increased dimensionality challenge
        f8 = 0.05 * np.sum(x_norm[:-3] * x_norm[1:-2]**2 * x_norm[2:-1] * x_norm[3:])
        
        # Combined result with carefully tuned weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
        
        return result