import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced exponential decay terms with modified sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.exp(-0.15 * xi**2) * np.sin(4 * xi) + 0.3 * np.exp(-0.08 * xi**2) * np.cos(3 * xi) + 0.2 * xi**3
        
        # Add interaction terms between variables with cubic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2)) + 0.05 * (x[i] * x[j])**3
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.015 * np.random.random())
        
        return result