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
        
        # Quadratic terms
        for i in range(self.dim):
            result += 0.1 * x[i]**2
            
        # Sinusoidal perturbations to create local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * np.pi * x[i] / 5.0)
            
        # Additional cross-terms to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * x[i] * x[j] * np.sin(0.5 * np.pi * x[i] / 5.0) * np.sin(0.5 * np.pi * x[j] / 5.0)
                
        # Global minimum at origin
        return result