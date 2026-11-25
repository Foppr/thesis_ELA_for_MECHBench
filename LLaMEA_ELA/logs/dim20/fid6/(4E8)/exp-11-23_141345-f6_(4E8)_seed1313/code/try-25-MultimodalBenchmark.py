import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially scaled polynomial terms
        poly_term = np.sum(np.exp(0.3 * np.abs(x)) * x**4)
        
        # Multi-frequency sinusoidal oscillations with chaotic modulation
        sin_term = np.sum(np.sin(1.2 * x) * np.sin(0.9 * x) * np.sin(0.5 * x) * np.sin(0.3 * x))
        
        # Higher-order cross-term interactions with exponential coupling
        cross_term = np.sum(np.exp(0.2 * np.abs(x[:-1])) * x[:-1]**3 * x[1:]**3)
        
        # Additional chaotic quadratic interaction
        chaotic_quad = np.sum((x[:-2]**2 + x[1:-1]**2 + x[2:]**2) * np.sin(x[:-2] * x[1:-1] * x[2:]))
        
        # Combined function with increased complexity and varied weights
        return 0.25 * poly_term + 0.5 * sin_term + 0.1 * cross_term + 0.15 * chaotic_quad