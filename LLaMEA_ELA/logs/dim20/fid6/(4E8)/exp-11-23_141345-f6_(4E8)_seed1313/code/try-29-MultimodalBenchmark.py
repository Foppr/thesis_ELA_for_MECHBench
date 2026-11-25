import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms
        exp_term = np.sum(np.exp(-0.1 * x**2))
        
        # Trigonometric coupling with varying frequencies
        trig_term = np.sum(np.cos(0.5 * x) * np.sin(0.3 * x) * np.cos(0.1 * x))
        
        # Radial symmetry with polynomial scaling
        radial_term = np.sum(x**2 * np.exp(-0.05 * np.sum(x**2)))
        
        # Combined function with adjusted weights
        return 0.2 * exp_term + 0.5 * trig_term + 0.3 * radial_term