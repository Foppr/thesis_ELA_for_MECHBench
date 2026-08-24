import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Additional high-frequency sinusoidal component for increased complexity
        high_freq = np.sum(np.sin(10 * np.pi * x_normalized**2))
        
        # Product of all dimensions (creates correlation between variables)
        product = np.prod(x_normalized)
        
        # Additional polynomial term for varied curvature
        polynomial = np.sum(x_normalized**4)
        
        # Combined function with multiple local minima
        return quadratic + 0.1 * sinusoidal + 0.01 * product + 0.05 * high_freq + 0.005 * polynomial