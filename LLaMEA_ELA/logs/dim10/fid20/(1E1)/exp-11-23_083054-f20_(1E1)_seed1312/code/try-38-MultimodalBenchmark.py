import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with non-linear frequency modulation
        f2 = np.sum(np.sin(6 * np.pi * x_norm * (1 + 0.3 * np.sin(2 * np.pi * x_norm))) ** 2 + 
                   0.5 * np.sin(10 * np.pi * x_norm * (1 + 0.2 * np.cos(3 * np.pi * x_norm))) ** 2)
        
        # High-frequency chaotic interaction terms
        f3 = np.sum(np.sin(15 * np.pi * x_norm) ** 2 + 
                   0.3 * np.sin(20 * np.pi * x_norm) ** 2 + 
                   0.1 * np.sin(25 * np.pi * x_norm) ** 2)
        
        # Polynomial interaction terms with coupled exponents and modified weights
        f4 = np.sum(2.0 * x_norm**4 + 0.5 * x_norm**6 + 0.1 * x_norm**8)
        
        # Exponential barrier term to create deep, narrow basins
        f5 = np.sum(np.exp(-5.0 * np.abs(x_norm)) * (1 - np.exp(-2.0 * np.abs(x_norm))))
        
        # Coupled product term with chaotic scaling
        f6 = np.prod(0.7 * np.cos(0.5 * np.pi * x_norm * (1 + 0.1 * np.sin(4 * np.pi * x_norm))) ** 2 + 
                    0.3 * np.sin(0.9 * np.pi * x_norm * (1 + 0.05 * np.cos(5 * np.pi * x_norm))) ** 2)
        
        # Combine all terms with carefully tuned weights
        return 0.5 * f1 + 0.2 * f2 + 0.08 * f3 + 0.04 * f4 + 0.03 * f5 - 0.05 * f6