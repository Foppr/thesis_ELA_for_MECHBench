import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic component
        f1 = np.sum(x_norm**2)
        
        # Non-separable sine-cosine interaction term
        f2 = np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        # Cross-term interaction creating non-separability
        f3 = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Global ruggedness term with multiple local minima
        f4 = np.sum(np.sin(5 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Chaotic modulation component using logistic map
        chaotic = 0.0
        r = 3.99
        for i in range(self.dim - 1):
            chaotic += np.sin(r * x_norm[i] * (1 - x_norm[i]))
        
        # Modified weights and enhanced sinusoidal modulation for increased difficulty
        return 0.6 * f1 + 1.8 * f2 + 0.9 * f3 + 2.2 * f4 + 0.4 * chaotic