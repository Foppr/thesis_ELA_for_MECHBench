import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sinusoidal components with varying frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Additional penalty term with shifted sinusoids
        result += 0.02 * np.sum(np.abs(x - 1.0))
        
        return result