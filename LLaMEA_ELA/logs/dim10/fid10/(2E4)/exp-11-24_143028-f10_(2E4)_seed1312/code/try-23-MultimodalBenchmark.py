import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Nested sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            result += 0.8 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            result += 0.5 * np.sin(4 * np.pi * x[i]) * np.cos(5 * np.pi * x[i])
        
        # Asymmetric saddle point structure
        for i in range(self.dim):
            result += 0.3 * x[i]**4 - 0.6 * x[i]**3 + 0.2 * x[i]**2
        
        # Dynamic interaction terms based on pairwise differences
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                result += 0.4 * np.sin(7 * diff) * np.cos(9 * diff) * (1 + 0.1 * np.abs(diff))
        
        # Non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.7 * np.sin(20 * sum_x) * np.cos(18 * sum_x)
        
        # Chaotic component with exponential scaling
        chaotic_term = 0.2 * np.prod(np.sin(3 * x + 0.5))
        result += chaotic_term
        
        # Asymmetric penalty for large values
        result += 0.15 * np.sum(np.abs(x)**3)
        
        return result