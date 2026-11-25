import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with stronger attenuation and dimension-dependent coefficients
        exp_term = np.sum(np.exp(-0.2 * x**2) * np.cos(0.3 * x) * np.sin(0.1 * x))
        
        # Higher frequency trigonometric interactions with amplified coupling
        trig_term = np.sum(np.sin(1.5 * x) * np.cos(0.8 * x) * np.sin(0.4 * x) * np.cos(0.2 * x))
        
        # Radial symmetry with quadratic scaling and enhanced logarithmic interaction
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.1 * r_squared) * (1 + 0.1 * r_squared**2)
        
        # Stronger cross-dimensional coupling with polynomial and trigonometric interactions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.5 * x[:-1]) * np.cos(0.3 * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Additional high-frequency oscillation with cubic terms for increased multimodality
        high_freq_term = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) * np.sin(3.0 * x))
        
        # Combined function with adjusted weights for enhanced multimodality and convergence difficulty
        return 0.3 * exp_term + 0.4 * trig_term + 0.2 * radial_term + 0.05 * cross_term + 0.05 * high_freq_term