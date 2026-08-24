import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial chaos terms with sinusoidal coupling
        for i in range(self.dim):
            xi = x[i]
            result += (xi**4 - 6*xi**2 + 9) * np.sin(2 * xi) + 0.5 * (xi**3 - 3*xi) * np.cos(3 * xi)
        
        # Add coupled sinusoidal interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Add a dynamic conditioning factor based on dimensionality
        conditioning = 1.0 + 0.1 * np.sin(self.dim)
        result *= conditioning
        
        # Add noise
        result += 0.01 * np.random.random()
        
        return result