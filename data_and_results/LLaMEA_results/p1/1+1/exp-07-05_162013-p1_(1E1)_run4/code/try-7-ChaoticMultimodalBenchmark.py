import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay terms with chaotic behavior
        for i in range(self.dim):
            result += np.exp(-0.1 * np.abs(x[i])) * np.cos(2 * np.pi * x[i])
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(0.5 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Chaotic component using sine of exponential
        for i in range(self.dim):
            result += 0.2 * np.sin(np.exp(x[i] / 5.0))
            
        # Add a global minimum at origin with additional penalty
        result += 0.1 * np.sum(x**2)
        
        return result