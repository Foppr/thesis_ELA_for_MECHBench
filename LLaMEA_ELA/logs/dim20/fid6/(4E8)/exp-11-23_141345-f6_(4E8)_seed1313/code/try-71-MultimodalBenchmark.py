import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested exponential decay with multiple decay rates and enhanced attenuation
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.exp(-0.3 * x**4) * np.cos(0.2 * x) * np.sin(0.1 * x))
        
        # Higher-order trigonometric couplings with chaotic frequency modulation
        trig_term = np.sum(np.sin(2.0 * x + np.sin(0.5 * x)) * np.cos(1.5 * x + np.cos(0.3 * x)) * 
                          np.sin(0.8 * x + np.sin(0.7 * x)) * np.cos(0.4 * x + np.cos(0.6 * x)))
        
        # Radial symmetry with polynomial scaling and enhanced logarithmic interaction
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.05 * r_squared) * (1 + 0.2 * r_squared**3)
        
        # Cross-dimensional interactions with chaotic oscillations and higher-order couplings
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.7 * x[:-1]) * np.cos(0.5 * x[1:]) * 
                           (x[:-1]**3 + x[1:]**3) * np.sin(0.2 * (x[:-1]**2 + x[1:]**2)))
        
        # Additional high-frequency chaotic oscillation with cubic and quartic terms
        high_freq_term = np.sum(np.sin(6.0 * x + np.sin(3.0 * x)) * 
                               np.cos(5.0 * x + np.cos(2.0 * x)) * 
                               np.sin(4.0 * x + np.sin(1.5 * x)) * 
                               np.cos(3.0 * x + np.cos(1.0 * x)))
        
        # Combined function with adjusted weights for enhanced multimodality and convergence difficulty
        return 0.25 * exp_term + 0.35 * trig_term + 0.2 * radial_term + 0.1 * cross_term + 0.1 * high_freq_term