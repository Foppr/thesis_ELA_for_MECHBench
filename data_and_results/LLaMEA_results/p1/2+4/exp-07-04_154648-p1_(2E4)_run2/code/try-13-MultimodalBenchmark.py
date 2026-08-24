import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic terms with different coefficients
        for i in range(self.dim):
            result += (i + 1) * x[i]**2
        
        # Modified sinusoidal perturbations with higher frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Higher-order polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x[i]**3 * x[j]**2 * np.sin(x[i] + x[j])
        
        # Additional cross-term with cubic interaction
        for i in range(self.dim):
            result += 0.05 * x[i]**3
        
        return result