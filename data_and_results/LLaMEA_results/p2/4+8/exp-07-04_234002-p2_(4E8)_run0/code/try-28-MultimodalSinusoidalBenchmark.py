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
            result += 0.9 * np.sin(1.3 * x[i]) * np.cos(0.6 * x[i]) + 0.2 * x[i]**2 + 0.03 * x[i]**3
            
        # Add interaction terms between dimensions with different coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * np.sin(1.6 * x[i]) * np.sin(0.9 * x[j]) + 0.015 * x[i] * x[j]
                
        # Add a global scaling factor with additional quadratic and quartic terms
        result = result * (1.0 + 0.2 * np.sum(x**2) + 0.07 * np.sum(x**4) + 0.02 * np.sum(x**6))
        
        return result