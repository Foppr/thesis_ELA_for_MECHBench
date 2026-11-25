import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential growth component with chaotic behavior
        for i in range(self.dim):
            result += np.exp(0.1 * x[i]**2) - 1.0
        
        # Sinusoidal modulation to create multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i])
        
        # Cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim - 1):
            result += 0.3 * np.exp(-0.5 * (x[i]**2 + x[i+1]**2)) * np.sin(3 * x[i] * x[i+1])
        
        # Additional chaotic term with polynomial interaction
        for i in range(self.dim):
            result += 0.2 * x[i]**4 - 0.8 * x[i]**2
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result