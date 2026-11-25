import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base term with mixed degrees
        f1 = np.sum(x_norm**6 + 0.5 * x_norm**4 + 0.1 * x_norm**2)
        
        # High-frequency trigonometric oscillations
        f2 = np.sum(np.sin(20 * x_norm) * np.cos(10 * x_norm))
        
        # Logarithmic barrier terms to create complex valleys
        f3 = np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.sin(5 * np.pi * x_norm))
        
        # Product of sinusoids with varying frequencies for multi-scale structure
        f4 = np.prod(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) + 0.5)
        
        # Exponential decay interaction term
        f5 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(3 * np.pi * x_norm))
        
        # Cross-term interaction creating non-separable structure
        f6 = np.sum((x_norm[:-1] + x_norm[1:]) * np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Dimensionality-dependent scaling
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all terms with different weights
        result = dim_factor * (0.4 * f1 + 0.3 * f2 - 0.2 * f3 + 0.1 * f4 + 0.05 * f5 + 0.05 * f6)
        
        # Add small fifth-order polynomial for additional complexity
        result += 0.02 * np.sum(x_norm**5)
        
        return result