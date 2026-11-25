import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.cos(0.15 * x))
        
        # Coupled trigonometric interactions with higher frequencies and amplitudes
        trig_term = np.sum(np.sin(1.2 * x) * np.cos(0.8 * x) * np.sin(0.6 * x) * np.cos(0.3 * x))
        
        # Radial symmetry with logarithmic scaling and enhanced cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.15 * r_squared) * np.log(1 + 0.2 * r_squared)
        
        # Cross-dimensional coupling with polynomial interactions and interaction coefficients
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.5 * x[:-1]) * np.cos(0.4 * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Additional high-frequency oscillatory component for increased multimodality
        osc_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.05 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality and complexity
        return 0.25 * exp_term + 0.35 * trig_term + 0.25 * radial_term + 0.1 * cross_term + 0.05 * osc_term