import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different coefficients
        # and sinusoidal perturbations to create multiple local minima
        result = 0.0
        
        # Quadratic component (global minimum at origin)
        for i in range(self.dim):
            result += x[i]**2
        
        # Add sinusoidal perturbations to create multiple local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add coupling terms between dimensions
        for i in range(self.dim - 1):
            result += 0.05 * (x[i] - x[i+1])**2
        
        return result