import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with radial symmetry
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.cos(2.0 * x))
        
        # Trigonometric interactions with varying frequencies
        trig_term = np.sum(np.sin(3.0 * x) * np.cos(1.5 * x) * np.sin(0.5 * x))
        
        # Radial component with polynomial scaling
        radial_term = np.sum(x**2 * np.exp(-0.05 * np.sum(x**2)))
        
        # Cross-term interactions with sinusoidal modulation
        cross_term = np.sum(np.sin(x[:-1] + x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Combined function with adjusted weights
        return 0.25 * exp_term + 0.4 * trig_term + 0.15 * radial_term + 0.2 * cross_term