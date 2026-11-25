import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with exponential scaling
        poly_term = np.sum(np.exp(0.5 * x**2) * x**6)
        
        # Complex sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.sin(0.7 * x) * np.cos(0.3 * x))
        
        # Advanced cross-term interactions with exponential coupling
        cross_term = np.sum(np.exp(x[:-1] * x[1:]) * (x[:-1]**3 + x[1:]**3))
        
        # Additional radial symmetry with logarithmic scaling
        radial_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(np.pi * x))
        
        # Combined function with increased complexity and varied weights
        return 0.4 * poly_term + 0.4 * sin_term + 0.15 * cross_term + 0.05 * radial_term