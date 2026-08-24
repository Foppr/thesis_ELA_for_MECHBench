import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with modified frequencies
        for i in range(self.dim):
            result += 0.8 * np.sin(1.2 * x[i]) * np.cos(0.7 * x[i]) + 0.15 * x[i]**2 + 0.02 * x[i]**3
            
        # Add interaction terms between dimensions with different coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(1.5 * x[i]) * np.sin(0.8 * x[j]) + 0.01 * x[i] * x[j]
                
        # Add a global scaling factor with additional quadratic term
        result = result * (1.0 + 0.15 * np.sum(x**2) + 0.05 * np.sum(x**4))
        
        return result