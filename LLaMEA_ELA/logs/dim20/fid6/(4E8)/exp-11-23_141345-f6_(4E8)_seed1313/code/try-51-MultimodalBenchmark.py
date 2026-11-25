import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.15 * x**2) * np.cos(0.15 * x))
        
        # Coupled trigonometric interactions with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(0.6 * x) * np.cos(0.35 * x) * np.sin(0.25 * x) * np.cos(0.07 * x))
        
        # Radial symmetry with logarithmic scaling and cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.12 * r_squared) * np.log(1 + 0.12 * r_squared)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.35 * x[:-1]) * np.cos(0.25 * x[1:]))
        
        # Combined function with adjusted weights for enhanced multimodality
        return 0.35 * exp_term + 0.45 * trig_term + 0.18 * radial_term + 0.02 * cross_term