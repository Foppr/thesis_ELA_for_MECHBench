import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2)
        
        # Sinusoidal oscillations to create multiple local minima
        sinusoidal = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Additional multimodal component with different frequencies
        multimodal = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Combine components with different weights
        result = 0.5 * polynomial + 0.3 * sinusoidal + 0.2 * multimodal
        
        return result