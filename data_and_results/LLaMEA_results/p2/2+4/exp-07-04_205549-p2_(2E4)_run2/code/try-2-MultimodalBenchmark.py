import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Shift and scale to [-1, 1] for the main function
        x_scaled = x / 5.0
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different coefficients
        # and sinusoidal terms to create multiple local minima
        result = 0.0
        
        # Main quadratic terms
        for i in range(self.dim):
            result += (x_scaled[i] - 0.5)**2
        
        # Add sinusoidal terms for multimodality
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * np.pi * x_scaled[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(3 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # Add a global minimum at the origin
        result += 0.5 * np.sum(x_scaled**2)
        
        return result