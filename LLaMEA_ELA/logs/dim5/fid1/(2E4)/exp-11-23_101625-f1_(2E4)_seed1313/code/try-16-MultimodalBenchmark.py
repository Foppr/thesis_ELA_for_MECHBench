import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced multimodal components with higher frequencies and modified amplitudes
        for i in range(self.dim):
            result += 0.3 * np.cos(12 * x[i]) * np.exp(-0.15 * (x[i] - 1)**2) + 0.1 * np.sin(8 * x[i])
            
        # Stronger interaction terms between dimensions with varying coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.07 * np.sin(6 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.08 * (x[i] - x[j])**2) + \
                         0.03 * np.cos(7 * x[i]) * np.sin(3 * x[j])
                
        # Additional cross-dimensional penalty with varied coefficients and non-linear terms
        for i in range(self.dim):
            result += 0.15 * (x[i] - 2)**4 + 0.08 * np.sin(7 * x[i]) + 0.05 * np.cos(9 * x[i])
            
        # Global minimum modification with non-linear transformation and additional harmonic terms
        result += 0.15 * np.sum((x - 1)**4) + 0.05 * np.sum(np.sin(5 * x))
        
        # Add a complex landscape component to increase challenge
        complex_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complex_term += 0.02 * np.sin(3 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        result += complex_term
        
        return result