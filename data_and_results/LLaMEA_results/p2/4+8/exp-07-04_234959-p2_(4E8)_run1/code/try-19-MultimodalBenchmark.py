import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal term with multiple local minima using higher frequency sinusoids
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_normalized)**6)
        
        # Additional penalty term with different power law for radial complexity
        f3 = 0.02 * np.sum(np.abs(x_normalized)**0.3)
        
        # Radial interaction term to create more complex landscape
        radial_term = 0.05 * (np.sum(x_normalized**2)**2)
        
        return f1 + f2 + f3 + radial_term