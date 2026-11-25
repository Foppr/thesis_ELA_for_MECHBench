import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multi-scale oscillations
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.sin(0.6 * x) * np.cos(0.4 * x))
        
        # Higher-order trigonometric couplings with varying phase shifts and amplitude modulation
        trig_term = np.sum((np.sin(1.5 * x)**4 + 0.5 * np.sin(0.8 * x)**3) * 
                          (np.cos(0.9 * x)**2 + 0.3 * np.cos(0.5 * x)) * 
                          np.sin(0.3 * x) * np.cos(0.2 * x))
        
        # Enhanced radial symmetry with polynomial scaling and logarithmic modulation
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.15 * r_squared) * (1 + 0.15 * r_squared**2) * np.log(1 + 0.03 * r_squared)
        
        # Cross-dimensional coupling with chaotic sine-cosine interactions and dynamic phase shifts
        cross_term = np.sum(np.sin(x[:-1] * x[1:] + 0.1 * x[:-1]**2) * 
                           np.cos(x[:-1] + x[1:] + 0.05 * x[1:]**2) * 
                           np.sin(0.4 * x[:-1]) * np.cos(0.3 * x[1:]))
        
        # Additional chaotic high-frequency oscillation with variable frequency for extreme multimodality
        high_freq_term = np.sum(np.sin(6.0 * x + 0.2 * x**2) * 
                               np.cos(5.0 * x + 0.1 * x**3) * 
                               np.sin(4.0 * x + 0.15 * x**2) * 
                               np.cos(3.0 * x + 0.05 * x**3))
        
        # Combined function with increased complexity and diverse curvature properties
        return 0.25 * exp_term + 0.2 * trig_term + 0.25 * radial_term + 0.18 * cross_term + 0.12 * high_freq_term