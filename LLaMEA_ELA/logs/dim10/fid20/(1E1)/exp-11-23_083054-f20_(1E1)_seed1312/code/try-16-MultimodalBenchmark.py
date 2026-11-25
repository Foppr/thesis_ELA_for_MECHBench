import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with irrational frequencies to increase complexity
        f2 = np.sum(np.sin(np.pi * np.sqrt(2) * x_norm) ** 2 + 
                   0.7 * np.sin(np.pi * np.sqrt(3) * x_norm) ** 2 + 
                   0.4 * np.sin(np.pi * np.sqrt(5) * x_norm) ** 2)
        
        # Exponential interaction terms to create sharp gradients and plateaus
        f3 = np.sum(1.2 * np.exp(-x_norm**2) + 0.8 * np.exp(-(x_norm - 0.5)**2) + 
                   0.6 * np.exp(-(x_norm + 0.3)**2))
        
        # High-dimensional coupling through product of transformed variables
        f4 = np.sum(np.prod(np.sin(2 * np.pi * x_norm) ** 2 + 
                           0.5 * np.cos(3 * np.pi * x_norm) ** 2, axis=0))
        
        # Cross-dimensional interaction with modified scaling factors
        f5 = np.sum(0.5 * np.sin(10 * x_norm) ** 4 + 0.3 * np.cos(15 * x_norm) ** 4)
        
        # Combined landscape with altered weights for increased discrimination
        return 0.5 * f1 + 0.3 * f2 + 0.1 * f3 + 0.05 * f4 - 0.05 * f5