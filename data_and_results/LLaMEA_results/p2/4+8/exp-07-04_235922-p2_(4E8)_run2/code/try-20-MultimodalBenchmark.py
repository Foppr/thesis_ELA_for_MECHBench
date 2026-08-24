import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add modified exponential decay terms with enhanced sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.exp(-0.15 * xi**2) * np.sin(4 * xi) + 0.3 * np.exp(-0.08 * xi**2) * np.cos(3 * xi) + 0.2 * np.sin(5 * xi) * np.cos(2 * xi)
        
        # Add more complex interaction terms between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) + 0.05 * np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.02 * np.random.random())
        
        return result