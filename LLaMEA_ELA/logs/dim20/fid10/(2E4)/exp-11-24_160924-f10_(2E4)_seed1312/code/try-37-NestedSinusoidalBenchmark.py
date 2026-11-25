import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add nested sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Nested modulation using multiple sine waves with different periods and amplitudes
            result += (np.sin(xi) + 0.5 * np.sin(3 * xi) + 0.2 * np.sin(7 * xi)) * \
                      (1 + 0.3 * np.cos(2 * xi) + 0.1 * np.cos(5 * xi))
            
        # Add cross-dimensional interaction terms with nested structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce non-separable interactions with varying coupling strength
                coupling_strength = 0.1 + 0.05 * np.sin(0.5 * (x[i] + x[j]))
                result += coupling_strength * np.sin(2 * (x[i]**2 + x[j]**2)) * \
                          np.cos(0.7 * (x[i] - x[j]))
                
        # Add a global scaling term with polynomial and exponential components
        result += 0.05 * np.sum(np.abs(x)**3) + 0.02 * np.sum(np.exp(-0.1 * x**2))
        
        # Introduce a complex interaction involving all variables through a nested structure
        mean_x = np.mean(x)
        result += 0.3 * np.sin(5 * mean_x) * np.cos(3 * np.sum(x**2)) + \
                  0.2 * np.exp(-0.05 * np.sum((x - mean_x)**4))
        
        return result