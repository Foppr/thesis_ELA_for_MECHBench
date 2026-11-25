import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        sum_squares = np.sum(x_norm**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(5 * np.pi * x_norm[i])**6
        
        # Additional quadratic term to control condition number
        quadratic = 0.1 * np.sum(x_norm**4)
        
        return sum_squares + multimodal + quadratic