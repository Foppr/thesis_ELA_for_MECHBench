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
            result += (0.8 * np.sin(2.5 * xi) * np.exp(-0.15 * xi**2) + 
                      0.6 * np.cos(3.5 * xi) * np.exp(-0.08 * xi**2) + 
                      0.4 * np.sin(4.5 * xi) * np.exp(-0.03 * xi**2))
        
        # Add interaction terms with polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-term with exponential decay
                cross_term = np.exp(-0.02 * (x[i]**2 + x[j]**2)) * (x[i]**2 + x[j]**2)
                result += 0.3 * np.sin(1.5 * x[i] * x[j]) * cross_term
        
        # Add cubic and quartic interaction terms for increased complexity
        for i in range(self.dim):
            result += 0.15 * x[i]**3 + 0.08 * x[i]**4
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.03 * np.random.random())
        
        return result