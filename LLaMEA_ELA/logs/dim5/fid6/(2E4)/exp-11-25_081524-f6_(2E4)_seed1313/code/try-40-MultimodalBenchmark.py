import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic chaotic modulation term
        log_modulation = np.sum(np.log(np.abs(x) + 1.0) * np.sin(x))
        
        # Saddle-point structure with polynomial interactions
        saddle = np.sum(x**2 - x**4 + 0.5 * x**6)
        
        # Non-uniform scaling to increase conditioning difficulty
        scaling = np.sum((x**2 + 0.1) * (x**3 + 0.2))
        
        # Asymmetric cross-terms with exponential interactions
        exp_cross = np.sum(np.exp(0.5 * x[:-1]) * x[1:]**2) + np.sum(np.exp(-0.3 * x[:-2]) * x[2:]**3)
        
        # Add fractal-like self-similarity through recursive polynomial terms
        fractal = 0.05 * np.sum(x**3 * np.sin(2.0 * x))
        
        return log_modulation + saddle + scaling + exp_cross + fractal