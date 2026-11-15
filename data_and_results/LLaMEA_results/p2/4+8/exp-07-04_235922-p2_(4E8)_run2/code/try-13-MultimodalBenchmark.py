import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add exponential decay terms with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += np.exp(-0.1 * xi**2) * np.sin(3 * xi) + 0.5 * np.exp(-0.05 * xi**2) * np.cos(2 * xi)
        
        # Add interaction terms between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.01 * np.random.random())
        
        return result