import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        sinusoidal = np.sum(np.sin(10 * np.pi * x_norm) ** 2 + 
                           0.5 * np.sin(20 * np.pi * x_norm) ** 2 + 
                           0.3 * np.sin(30 * np.pi * x_norm) ** 2)
        
        # Exponentially increasing polynomial terms for complexity
        poly = np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # Cross-terms creating interaction between dimensions
        cross_terms = np.sum((x_norm[:-1] + x_norm[1:]) ** 4)
        
        # Additional oscillatory component with varying amplitude
        oscillatory = np.sum(np.sin(15 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        return quadratic + 0.2 * sinusoidal + 0.1 * poly + 0.05 * cross_terms + 0.02 * oscillatory