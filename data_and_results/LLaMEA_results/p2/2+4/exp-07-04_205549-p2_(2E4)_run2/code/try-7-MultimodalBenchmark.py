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
        
        # Main quadratic terms with varying coefficients
        for i in range(self.dim):
            result += (x_scaled[i] - 0.3)**2
        
        # Add sinusoidal terms for multimodality with different frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * np.pi * x_scaled[i]) + 0.05 * np.cos(4 * np.pi * x_scaled[i])
        
        # Add interaction terms between dimensions with higher frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(6 * np.pi * (x_scaled[i] + x_scaled[j])) + 0.03 * np.cos(3 * np.pi * (x_scaled[i] - x_scaled[j]))
        
        # Add a global minimum at the origin with modified quadratic term
        result += 0.3 * np.sum(x_scaled**2)
        
        return result