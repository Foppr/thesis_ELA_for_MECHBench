import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squared terms with different scales and offsets
        result = 0.0
        
        # Global minimum at origin
        result += np.sum(x**2)
        
        # Add multiple local minima using modified sinusoidal terms
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add coupling between variables to create complex landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * (x[i] - x[j])**2 * np.sin(2 * (x[i] + x[j]))
                
        return result