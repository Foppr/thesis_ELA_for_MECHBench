import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with modified coefficients
        exp_term = np.sum(np.exp(-0.15 * x**2) * np.cos(0.3 * x))
        
        # Coupled trigonometric interactions with changed frequencies and amplitudes
        trig_term = np.sum(np.sin(0.9 * x) * np.cos(0.4 * x) * np.sin(0.15 * x) * np.cos(0.1 * x))
        
        # Radial symmetry with modified logarithmic scaling and cross-term interactions
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.08 * r_squared) * np.log(1 + 0.08 * r_squared)
        
        # Cross-dimensional coupling with altered polynomial interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.25 * x[:-1]) * np.cos(0.15 * x[1:]))
        
        # Additional high-frequency oscillation for increased multimodality
        high_freq_term = np.sum(np.sin(3.5 * x) * np.cos(2.5 * x))
        
        # Introduce a new component to enhance landscape complexity
        complex_term = np.sum(np.sin(1.8 * x) * np.cos(1.5 * x) * np.exp(-0.03 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality
        return 0.25 * exp_term + 0.30 * trig_term + 0.15 * radial_term + 0.15 * cross_term + 0.08 * high_freq_term + 0.07 * complex_term