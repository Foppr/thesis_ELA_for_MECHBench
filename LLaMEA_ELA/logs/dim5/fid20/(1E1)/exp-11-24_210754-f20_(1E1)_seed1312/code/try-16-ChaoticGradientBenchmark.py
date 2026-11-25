import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic sine wave with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10.0 * x * np.sin(3.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Nested periodic structure with exponential decay
        f3 = 0.5 * np.sum(np.sin(np.pi * x) * np.cos(2.0 * np.pi * x) * np.exp(-0.05 * x**2))
        
        # Saddle point enhancement using product of trigonometric functions
        f4 = 0.3 * np.sum(np.sin(x) * np.cos(x) * np.tan(0.5 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Exponential barrier regions to create sharp local minima
        f5 = 0.4 * np.sum(np.exp(-10.0 / (1.0 + np.exp(-x))) * np.sin(5.0 * x))
        
        # Add noise-like component with chaotic behavior
        f6 = 0.1 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(0.3 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6