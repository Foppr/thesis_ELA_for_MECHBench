import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different coefficients and offsets
        result = 0.0
        
        # Main quadratic term (global minimum at origin)
        result += np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Add a second set of local minima with different frequencies and amplitudes
        for i in range(self.dim):
            result += 0.08 * np.sin(8 * x[i])**2
            
        # Add coupling terms between dimensions to increase complexity
        for i in range(self.dim - 1):
            result += 0.03 * (x[i] - x[i+1])**2
            
        # Add coupling terms between all dimensions to create a more complex landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(x[i] + x[j])
                
        return result