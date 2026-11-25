import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial oscillations with varying degrees
        poly_osc = np.sum((x**2 + 0.1 * np.sin(10 * x)) ** 2)
        
        # Radial basis function components with varying centers and widths
        rbfs = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i, center in enumerate(centers):
            width = 0.5 + 0.5 * (i / max(1, self.dim - 1))
            rbfs += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # Cross-term interactions with sinusoidal modulation
        cross_terms = 0.0
        for i in range(self.dim - 1):
            cross_terms += np.sin(x[i] * x[i+1]) * (1 + 0.1 * np.abs(x[i] - x[i+1]))
        
        # Combined function value
        return condition_factor * poly_osc + rbfs + cross_terms