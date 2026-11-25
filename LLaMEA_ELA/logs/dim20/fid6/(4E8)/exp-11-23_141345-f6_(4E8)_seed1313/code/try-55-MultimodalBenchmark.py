import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.2 * x**2) * np.cos(0.1 * x))
        
        # Coupled trigonometric interactions with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * np.sin(0.2 * x) * np.cos(0.05 * x))
        
        # Radial symmetry with logarithmic scaling and cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.1 * r_squared) * np.log(1 + 0.1 * r_squared)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.3 * x[:-1]) * np.cos(0.2 * x[1:]))
        
        # Combined function with adjusted weights for enhanced multimodality
        return 0.3 * exp_term + 0.4 * trig_term + 0.2 * radial_term + 0.1 * cross_term