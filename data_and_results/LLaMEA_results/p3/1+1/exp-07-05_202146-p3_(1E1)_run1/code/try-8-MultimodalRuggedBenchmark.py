import numpy as np

class MultimodalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Add exponential decay interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.5 * np.exp(-dist) * np.sin(x[i] * x[j])
                
        # Add trigonometric coupling terms
        for i in range(self.dim):
            result += 0.3 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Add multimodal components with different scales
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(7 * x[i]) + 0.05 * np.sin(11 * x[i])**2
            
        # Add a rugged landscape component using step functions
        for i in range(self.dim):
            result += 0.2 * np.floor(np.abs(x[i]) / 1.5) * np.sin(x[i])
            
        # Add a global optimum enforcing term
        result += 0.01 * np.sum(np.abs(x)**3)
        
        # Add a complex interaction term involving all variables
        prod_x = np.prod(x)
        result += 0.15 * np.sin(np.pi * prod_x) * np.cos(2 * np.pi * prod_x)
        
        return result