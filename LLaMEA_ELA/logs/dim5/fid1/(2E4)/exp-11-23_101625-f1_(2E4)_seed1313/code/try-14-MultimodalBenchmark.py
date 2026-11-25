import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced multimodal components with higher frequencies
        for i in range(self.dim):
            result += 0.2 * np.cos(10 * x[i]) * np.exp(-0.2 * (x[i] - 1)**2)
            
        # Stronger interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Additional cross-dimensional penalty with varied coefficients
        for i in range(self.dim):
            result += 0.1 * (x[i] - 2)**4 + 0.05 * np.sin(6 * x[i])
            
        # Global minimum modification with non-linear transformation
        result += 0.1 * np.sum((x - 1)**4)
        
        return result