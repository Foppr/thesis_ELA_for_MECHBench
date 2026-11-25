import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal perturbations creating many local minima
        f2 = 0.5 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Logarithmic barrier terms to increase conditioning difficulty
        f3 = 0.1 * np.sum(np.log(np.abs(x_norm) + 1e-8))
        
        # Hyperbolic tangent nonlinearity for enhanced non-convexity
        f4 = 0.05 * np.sum(np.tanh(3 * x_norm)**2)
        
        # Exponentially scaled sinusoidal terms for complex landscape
        f5 = 0.3 * np.sum(np.exp(2 * np.sin(np.pi * x_norm)) - 1)
        
        # Combine all terms with varying weights
        return f1 + f2 + f3 + f4 + f5