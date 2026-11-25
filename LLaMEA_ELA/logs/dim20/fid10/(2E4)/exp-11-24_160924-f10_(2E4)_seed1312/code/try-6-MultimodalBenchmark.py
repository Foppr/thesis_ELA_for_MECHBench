import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        sum_squares = np.sum(x_normalized**2)
        
        # Multimodal term with multiple local minima and nonlinear interactions
        multimodal = 0.0
        for i in range(self.dim):
            # Add shifted sinusoidal terms with varying frequencies
            multimodal += (np.sin(7 * np.pi * x_normalized[i]) ** 4) + \
                         0.5 * (np.cos(3 * np.pi * x_normalized[i]) ** 2)
        
        # Combined function with different weights
        return sum_squares + 0.15 * multimodal