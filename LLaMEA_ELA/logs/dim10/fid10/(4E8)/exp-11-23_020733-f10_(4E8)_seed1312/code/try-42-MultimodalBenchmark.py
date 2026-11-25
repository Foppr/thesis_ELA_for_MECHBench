import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Higher-order polynomial term with modified weights to create complex valleys and ridges
        f1 = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**4 + 0.2 * x_norm**2)
        
        # Multiple trigonometric terms with altered frequencies creating denser local minima
        f2 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) + 
                   0.3 * np.sin(15 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm))
        
        # Exponential barrier term with modified parameters for sharper gradients
        f3 = np.sum(np.exp(-x_norm**2) - 1 + 0.3 * np.exp(-x_norm**2 / 0.3) - 0.3)
        
        # Additional cubic interaction terms to increase conditioning difficulty
        f4 = np.sum((x_norm[:-2] - x_norm[1:-1])**3)
        
        # Combined function with competing forces and increased complexity
        return 0.35 * f1 + 0.35 * f2 + 0.2 * f3 + 0.1 * f4