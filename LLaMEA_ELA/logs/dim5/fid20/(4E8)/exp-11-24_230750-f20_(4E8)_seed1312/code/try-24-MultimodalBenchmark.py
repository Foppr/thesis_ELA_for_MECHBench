import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with modified coefficients
        polynomial = 0.5 * np.sum(x**2) + 0.05 * np.sum(x**4)
        
        # Sinusoidal oscillations with different frequency
        sinusoidal = np.sum(np.sin(7.0 * x))
        
        # Cross-term interactions with exponential decay
        cross_terms = 0.3 * np.sum(x[:-1] * x[1:] * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Additional exponential decay term to create rugged landscape
        decay_term = 0.2 * np.sum(np.exp(-0.5 * x**2))
        
        # Combined function value
        return polynomial + sinusoidal + cross_terms + decay_term