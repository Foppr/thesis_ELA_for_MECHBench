import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.12 * x**2) * np.cos(0.25 * x))
        
        # Coupled trigonometric interactions with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(0.85 * x) * np.cos(0.35 * x) * np.sin(0.12 * x) * np.cos(0.08 * x))
        
        # Radial symmetry with logarithmic scaling and cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.06 * r_squared) * np.log(1 + 0.06 * r_squared)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.22 * x[:-1]) * np.cos(0.12 * x[1:]))
        
        # Additional high-frequency oscillation for increased multimodality
        high_freq_term = np.sum(np.sin(3.2 * x) * np.cos(2.2 * x))
        
        # Introduce a new component to enhance landscape complexity and improve fitness score
        complex_term = np.sum(np.sin(1.6 * x) * np.cos(1.3 * x) * np.exp(-0.025 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality
        return 0.22 * exp_term + 0.32 * trig_term + 0.18 * radial_term + 0.16 * cross_term + 0.09 * high_freq_term + 0.03 * complex_term