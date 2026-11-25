import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squared terms with different weights
        term1 = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal components with higher frequency
        term2 = 0.2 * np.sum(np.sin(7 * np.pi * x_norm))
        
        # Add a more complex multimodal component with different polynomial power
        term3 = 0.1 * np.sum((x_norm**6) * np.cos(3 * np.pi * x_norm))
        
        # Add interaction terms between dimensions
        term4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Shift global minimum to a non-zero point
        shift = 0.1
        term5 = 0.1 * np.sum((x_norm - shift)**2)
        
        # Combine terms with different scaling factors
        result = term1 + term2 + term3 + term4 + term5
        
        return result