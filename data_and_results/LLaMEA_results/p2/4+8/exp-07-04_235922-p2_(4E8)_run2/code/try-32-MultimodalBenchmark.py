import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal waves with polynomial decay
        for i in range(self.dim):
            xi = x[i]
            result += (np.sin(2 * xi) * np.exp(-0.1 * xi**2) + 
                      0.5 * np.cos(3 * xi) * np.exp(-0.05 * xi**2) + 
                      0.3 * np.sin(5 * xi) * np.exp(-0.02 * xi**2))
        
        # Add interaction terms with polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-term with exponential decay
                cross_term = np.exp(-0.01 * (x[i]**2 + x[j]**2)) * (x[i]**2 + x[j]**2)
                result += 0.2 * np.sin(x[i] * x[j]) * cross_term
        
        # Add cubic and quartic interaction terms for increased complexity
        for i in range(self.dim):
            result += 0.1 * x[i]**3 + 0.05 * x[i]**4
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.02 * np.random.random())
        
        return result