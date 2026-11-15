import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal interactions with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm)**3)
        f3 = 0.25 * np.sum(np.sin(11 * np.pi * x_norm)**5 * np.cos(9 * np.pi * x_norm))
        f4 = 0.3 * np.sum(np.cos(13 * np.pi * x_norm)**7 * np.sin(5 * np.pi * x_norm)**2)
        
        # Asymmetric polynomial potentials with different exponents
        f5 = 0.15 * np.sum(np.where(x_norm > 0, x_norm**7, -0.5 * x_norm**5))
        f6 = 0.2 * np.sum(np.where(x_norm < 0, x_norm**6, -0.3 * x_norm**4))
        
        # Dynamically shifted global minimum using a chaotic map
        shift = np.sin(np.linspace(0, np.pi, self.dim)) * 0.3
        f7 = 0.1 * np.sum((x_norm - shift)**8)
        
        # Additional high-frequency oscillations
        f8 = 0.18 * np.sum(np.sin(20 * np.pi * x_norm)**6)
        f9 = 0.12 * np.sum(np.cos(18 * np.pi * x_norm)**9)
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9