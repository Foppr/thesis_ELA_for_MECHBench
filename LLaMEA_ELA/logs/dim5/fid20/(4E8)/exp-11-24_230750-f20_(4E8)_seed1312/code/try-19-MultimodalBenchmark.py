import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add sinusoidal modulation with higher frequency and amplitude to create more local minima
        f2 = 0.2 * np.sum(np.sin(8 * np.pi * x_norm))
        
        # Add a quartic term to create additional complexity
        f3 = 0.015 * np.sum(x_norm**4)
        
        # Add a sextic term for even more complexity
        f4 = 0.005 * np.sum(x_norm**6)
        
        # Add interaction terms between dimensions to increase conditioning difficulty
        f5 = 0.02 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + f4 + f5