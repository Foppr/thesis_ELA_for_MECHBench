import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add multiple local minima using combined sinusoidal terms
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
            
        # Add a more complex saddle point structure with higher-order interactions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                result += 0.1 * (x[i]**2 - x[i+1]**2)**2
                
        # Add a radial component to increase multimodality
        r = np.sqrt(np.sum(x**2))
        result += 0.15 * np.sin(10 * r) * np.cos(5 * r)
        
        return result