import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r_squared = np.sum(x_norm**2)
        radial_term = np.exp(-r_squared / 2.0)
        
        # Trigonometric oscillations creating multiple local minima
        trig_term = np.sum(np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm))
        
        # Cross-term creating coupling between dimensions
        cross_term = np.sum(x_norm[:-1] * x_norm[1:]) if self.dim > 1 else 0.0
        
        # Add a global scaling factor
        result = 1.0 - radial_term + 0.5 * trig_term + 0.1 * cross_term
        
        return result