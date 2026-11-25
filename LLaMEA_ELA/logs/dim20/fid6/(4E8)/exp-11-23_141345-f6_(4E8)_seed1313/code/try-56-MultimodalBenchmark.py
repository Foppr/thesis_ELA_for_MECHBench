import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested exponential decay with multi-scale oscillations
        exp_term = np.sum(np.exp(-0.05 * x**2) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Higher-order trigonometric couplings with varying phase shifts
        trig_term = np.sum(np.sin(1.2 * x)**3 * np.cos(0.7 * x)**2 * np.sin(0.4 * x) * np.cos(0.2 * x))
        
        # Enhanced radial symmetry with polynomial scaling and logarithmic modulation
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.1 * r_squared) * (1 + 0.1 * r_squared**2) * np.log(1 + 0.02 * r_squared)
        
        # Cross-dimensional coupling with chaotic sine-cosine interactions
        cross_term = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]) * np.sin(0.3 * x[:-1]) * np.cos(0.2 * x[1:]))
        
        # Additional chaotic high-frequency oscillation for extreme multimodality
        high_freq_term = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Combined function with increased complexity and diverse curvature properties
        return 0.3 * exp_term + 0.25 * trig_term + 0.2 * radial_term + 0.15 * cross_term + 0.1 * high_freq_term