import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Higher-order polynomial term with mixed degrees to create complex valleys and ridges
        f1 = np.sum(x_norm**6 + 0.7 * x_norm**4 + 0.3 * x_norm**2)
        
        # Multiple trigonometric terms with varying frequencies creating intricate local minima patterns
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) + 
                   0.5 * np.sin(11 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm))
        
        # Exponential barrier term with sharper gradients near boundaries
        f3 = np.sum(np.exp(-x_norm**2) - 1 + 0.1 * np.exp(-(x_norm**2)/0.5) - 0.1)
        
        # Additional coupling terms between dimensions to increase interaction complexity
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**4)
        
        # Combined function with competing forces and enhanced complexity
        return 0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4