import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Additional multimodal terms with local minima
        f2 = 0.4 * np.sum(np.sin(10 * np.pi * x_norm)**12)
        f3 = 0.2 * np.sum(np.cos(6 * np.pi * x_norm)**10)
        f4 = 0.1 * np.sum((x_norm - 0.3)**8)
        f5 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm)**6)
        f6 = 0.15 * np.sum(np.cos(7 * np.pi * x_norm)**7)
        
        # Chaotic sinusoidal interactions
        f7 = 0.25 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Asymmetric polynomial potentials
        f8 = 0.15 * np.sum(np.abs(x_norm)**4.0)
        
        # Dynamically shifted global minimum
        shift = 0.25
        f9 = 0.2 * np.sum((x_norm - shift)**5)
        
        # Additional high-frequency oscillations for increased complexity
        f10 = 0.1 * np.sum(np.sin(20 * np.pi * x_norm)**3)
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10