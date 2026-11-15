import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with sinusoidal components
        # This creates multiple local minima in a grid pattern
        result = 0.0
        
        # Main sinusoidal contribution
        for i in range(self.dim):
            result += np.sin(x[i]) * np.cos(0.5 * x[i]) + 0.1 * x[i]**2
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i]) * np.sin(x[j])
                
        # Add a global scaling factor
        result = result * (1.0 + 0.1 * np.sum(x**2))
        
        return result