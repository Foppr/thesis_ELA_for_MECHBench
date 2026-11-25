import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squared terms with different coefficients
        result = np.sum(x**2)
        
        # Add multiple local minima using modified sinusoidal components
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Add interaction terms between variables to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x[i] * x[j] * np.sin(x[i] + x[j])
        
        # Add a global minimum at origin with additional penalty terms
        result += 0.015 * np.sum(np.abs(x))
        
        return result