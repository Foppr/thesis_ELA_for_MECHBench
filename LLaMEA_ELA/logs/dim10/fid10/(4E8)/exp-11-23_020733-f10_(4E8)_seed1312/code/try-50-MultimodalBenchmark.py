import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Higher-order polynomial term with modified weights to create complex valleys and ridges
        f1 = np.sum(0.9 * x_norm**6 + 0.6 * x_norm**4 + 0.3 * x_norm**2)
        
        # Multiple trigonometric terms with altered frequencies creating denser local minima
        f2 = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm) + 
                   0.4 * np.sin(17 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm))
        
        # Exponential barrier term with modified parameters for sharper gradients
        f3 = np.sum(np.exp(-x_norm**2) - 1 + 0.4 * np.exp(-x_norm**2 / 0.25) - 0.4)
        
        # Additional cubic interaction terms to increase conditioning difficulty
        f4 = np.sum((x_norm[:-2] - x_norm[1:-1])**3 + 0.5 * (x_norm[:-1] - x_norm[1:])**3)
        
        # Chaotic component using logistic map dynamics for increased complexity
        chaotic = np.sum(0.1 * np.sin(20 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm))
        
        # Combined function with competing forces and increased complexity
        return 0.3 * f1 + 0.3 * f2 + 0.25 * f3 + 0.15 * f4 + 0.05 * chaotic