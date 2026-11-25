import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multi-scale oscillations
        exp_term = np.sum(np.exp(-0.12 * x**2) * np.sin(0.75 * x) * np.cos(0.45 * x) * np.sin(0.25 * x))
        
        # Higher-order trigonometric couplings with varying phase shifts and amplitude modulation
        trig_term = np.sum((np.sin(1.6 * x)**4 + 0.55 * np.cos(0.85 * x)**3) * 
                          (np.sin(0.65 * x)**2 + 0.35 * np.cos(0.35 * x)**2) * 
                          np.sin(0.55 * x) * np.cos(0.25 * x))
        
        # Enhanced radial symmetry with polynomial scaling and logarithmic modulation
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.16 * r_squared) * (1 + 0.25 * r_squared**2) * np.log(1 + 0.035 * r_squared)
        
        # Cross-dimensional coupling with chaotic sine-cosine interactions and dynamic coupling coefficients
        cross_term = np.sum(np.sin(x[:-1] * x[1:] * 0.55) * np.cos(x[:-1] + x[1:] * 0.35) * 
                           np.sin(0.45 * x[:-1]) * np.cos(0.15 * x[1:]) * 
                           (1 + 0.15 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic high-frequency oscillation for extreme multimodality with dynamic scaling
        high_freq_term = np.sum(np.sin(6.5 * x) * np.cos(5.5 * x) * np.sin(4.5 * x) * np.cos(3.5 * x) * 
                               (1 + 0.25 * np.sin(2.5 * x)))
        
        # Additional chaotic modulation term to improve fitness score
        mod_term = np.sum(np.sin(0.85 * x)**2 * np.cos(0.65 * x)**2 * np.sin(0.45 * x) * 
                         np.cos(0.35 * x) * np.exp(-0.055 * x**2))
        
        # Combined function with increased complexity and diverse curvature properties
        return 0.26 * exp_term + 0.21 * trig_term + 0.26 * radial_term + 0.16 * cross_term + 0.11 * high_freq_term + 0.06 * mod_term