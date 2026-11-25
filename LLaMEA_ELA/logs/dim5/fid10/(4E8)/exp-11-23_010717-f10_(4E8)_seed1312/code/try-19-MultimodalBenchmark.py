import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_sum = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple local minima
        sinusoidal_sum = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Add a penalty term for large values to create a more challenging landscape
        penalty = 0.1 * np.sum(x_normalized**4)
        
        # Combine all components to create a multimodal function
        return quadratic_sum + sinusoidal_sum + penalty