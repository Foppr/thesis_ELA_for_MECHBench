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
        
        # Quadratic terms with different coefficients
        for i in range(self.dim):
            result += (i + 1) * x[i]**2
        
        # Enhanced sinusoidal perturbations to create local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Additional cross-term interactions with higher frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x[i] * x[j] * np.sin(2 * (x[i] + x[j]))
        
        # Add a small cubic term for additional complexity
        for i in range(self.dim):
            result += 0.005 * x[i]**3
        
        return result