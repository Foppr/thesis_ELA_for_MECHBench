import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic term (global minimum at origin)
        result = np.sum(x**2)
        
        # Enhanced sinusoidal terms with multiple frequencies
        for i in range(self.dim):
            result += 15 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]) + 5 * np.sin(1.2 * x[i])
        
        # Higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 2 * x[i]**4 - 3 * x[i]**3
        
        # Exponential decay terms with different rates
        for i in range(self.dim):
            result += 3 * np.exp(-0.2 * x[i]**2) + 2 * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional interaction terms with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] + 0.3 * x[j])
        
        # Additional high-frequency oscillation for increased difficulty
        for i in range(self.dim):
            result += 8 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        return result