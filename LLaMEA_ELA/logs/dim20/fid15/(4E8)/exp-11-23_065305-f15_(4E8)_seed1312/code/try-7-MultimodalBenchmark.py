import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squared terms with different weights
        term1 = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal components
        term2 = 0.1 * np.sum(np.sin(5 * np.pi * x_norm))
        
        # Add a more complex multimodal component
        term3 = 0.05 * np.sum((x_norm**4) * np.cos(2 * np.pi * x_norm))
        
        # Combine terms with different scaling factors
        result = term1 + term2 + term3
        
        return result