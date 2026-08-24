import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        poly_term = np.sum(x**4) / 4.0 + np.sum(x**3) / 3.0 + np.sum(x**2) / 2.0 + np.sum(x)
        
        # Trigonometric components with varying frequencies
        trig_term = np.sum(np.sin(2.0 * np.pi * x)) + np.sum(np.cos(3.0 * np.pi * x))
        
        # Exponential penalty terms with multiple local minima
        exp_penalty = 0.0
        for i in range(self.dim):
            exp_penalty += np.exp(-0.5 * (x[i] - 2.0)**2) + np.exp(-0.5 * (x[i] + 2.0)**2)
        
        # Chaotic component using sine map
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(np.pi * x[i] * np.sin(x[i]))
        
        # Combine all terms with different weights
        result = 0.5 * poly_term + 0.3 * trig_term + 0.2 * exp_penalty + 0.1 * chaotic
        
        return result