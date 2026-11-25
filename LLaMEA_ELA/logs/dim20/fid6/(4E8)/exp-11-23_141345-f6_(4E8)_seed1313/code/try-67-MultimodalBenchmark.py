import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.cos(0.2 * x))
        
        # Coupled trigonometric interactions with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(0.8 * x) * np.cos(0.3 * x) * np.sin(0.1 * x) * np.cos(0.07 * x))
        
        # Radial symmetry with logarithmic scaling and cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.05 * r_squared) * np.log(1 + 0.05 * r_squared)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.2 * x[:-1]) * np.cos(0.1 * x[1:]))
        
        # Additional high-frequency oscillation for increased multimodality
        high_freq_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Introduce a new component to enhance landscape complexity and improve fitness score
        complex_term = np.sum(np.sin(1.5 * x) * np.cos(1.2 * x) * np.exp(-0.02 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality
        return 0.2 * exp_term + 0.3 * trig_term + 0.2 * radial_term + 0.15 * cross_term + 0.1 * high_freq_term + 0.05 * complex_term