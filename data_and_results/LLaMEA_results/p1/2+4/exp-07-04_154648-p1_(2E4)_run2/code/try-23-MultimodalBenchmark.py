import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Random shift vector for global minimum
        np.random.seed(42)
        self.shift = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Asymmetric polynomial potentials with varying degrees
        f1 = np.sum((x_norm + self.shift)**3)
        f2 = 0.5 * np.sum(np.abs(x_norm)**4)
        f3 = 0.3 * np.sum(np.sin(11 * np.pi * x_norm)**12)
        
        # Chaotic sinusoidal interactions with varying frequencies
        f4 = 0.2 * np.sum(np.cos(13 * np.pi * x_norm)**10)
        f5 = 0.15 * np.sum(np.sin(7 * np.pi * x_norm)**8)
        f6 = 0.1 * np.sum(np.cos(9 * np.pi * x_norm)**6)
        
        # Cross-dimensional chaotic interactions with more complex coupling
        cross_term = 0.08 * np.sum(np.sin(3 * np.pi * x_norm[:-1]) * np.cos(5 * np.pi * x_norm[1:]) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add a dynamic shift component that changes based on input magnitude
        dynamic_shift = 0.05 * np.sum(np.sin(2 * np.pi * np.abs(x_norm)) * np.cos(4 * np.pi * np.abs(x_norm)))
        
        # Additional chaotic interaction terms to increase complexity
        f7 = 0.08 * np.sum(np.sin(17 * np.pi * x_norm)**14)
        f8 = 0.06 * np.sum(np.cos(19 * np.pi * x_norm)**16)
        
        # Cross-dimensional interaction with exponential coupling
        exp_cross = 0.04 * np.sum(np.exp(-x_norm[:-1]**2) * np.sin(6 * np.pi * x_norm[1:]) * (x_norm[:-1]**3 + x_norm[1:]**3))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + cross_term + dynamic_shift + f7 + f8 + exp_cross