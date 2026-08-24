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
            result += 0.9 * np.exp(-0.2 * xi**2) * np.sin(5 * xi) + 0.4 * np.exp(-0.1 * xi**2) * np.cos(4 * xi) + 0.25 * xi**4
        
        # Add interaction terms between variables with quartic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2)) + 0.1 * (x[i] * x[j])**4
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.02 * np.random.random())
        
        return result