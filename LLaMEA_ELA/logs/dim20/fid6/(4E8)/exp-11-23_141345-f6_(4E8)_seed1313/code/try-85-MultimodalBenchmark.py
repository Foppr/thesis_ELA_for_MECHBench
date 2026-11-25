import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multi-scale oscillations
        exp_term = np.sum(np.exp(-0.12 * x**2) * np.sin(0.7 * x) * np.cos(0.5 * x))
        
        # Higher-order trigonometric couplings with varying phase shifts and amplitude modulation
        trig_term = np.sum((np.sin(1.6 * x)**4 + 0.6 * np.sin(0.9 * x)**3) * 
                          (np.cos(1.0 * x)**2 + 0.4 * np.cos(0.6 * x)) * 
                          np.sin(0.4 * x) * np.cos(0.3 * x))
        
        # Enhanced radial symmetry with polynomial scaling and logarithmic modulation
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.18 * r_squared) * (1 + 0.2 * r_squared**2) * np.log(1 + 0.04 * r_squared)
        
        # Cross-dimensional coupling with chaotic sine-cosine interactions and dynamic phase shifts
        cross_term = np.sum(np.sin(x[:-1] * x[1:] + 0.15 * x[:-1]**2) * 
                           np.cos(x[:-1] + x[1:] + 0.08 * x[1:]**2) * 
                           np.sin(0.5 * x[:-1]) * np.cos(0.4 * x[1:]))
        
        # Additional chaotic high-frequency oscillation with variable frequency for extreme multimodality
        high_freq_term = np.sum(np.sin(7.0 * x + 0.25 * x**2) * 
                               np.cos(6.0 * x + 0.12 * x**3) * 
                               np.sin(5.0 * x + 0.18 * x**2) * 
                               np.cos(4.0 * x + 0.07 * x**3))
        
        # Combined function with increased complexity and diverse curvature properties
        return 0.26 * exp_term + 0.21 * trig_term + 0.26 * radial_term + 0.19 * cross_term + 0.13 * high_freq_term