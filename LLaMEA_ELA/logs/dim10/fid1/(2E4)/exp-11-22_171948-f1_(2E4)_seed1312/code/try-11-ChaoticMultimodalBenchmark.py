import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential growth component with modified chaotic behavior
        for i in range(self.dim):
            result += np.exp(0.15 * x[i]**2) - 1.0
        
        # Sinusoidal modulation with altered frequencies to create more local minima
        for i in range(self.dim):
            result += 0.6 * np.sin(12 * x[i]) * np.cos(8 * x[i])
        
        # Cross-dimensional coupling with different interaction terms
        for i in range(self.dim - 1):
            result += 0.4 * np.exp(-0.3 * (x[i]**2 + x[i+1]**2)) * np.sin(4 * x[i] * x[i+1])
        
        # Additional chaotic term with modified polynomial interaction
        for i in range(self.dim):
            result += 0.25 * x[i]**4 - 0.9 * x[i]**2
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result