import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multi-scale oscillations and dynamic scaling
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.sin(0.7 * x) * np.cos(0.4 * x) * np.sin(0.2 * x) * 
                         (1 + 0.1 * np.sin(3.0 * x)))
        
        # Higher-order trigonometric couplings with varying phase shifts, amplitude modulation, and chaotic interactions
        trig_term = np.sum((np.sin(1.5 * x)**4 + 0.5 * np.cos(0.8 * x)**3) * 
                          (np.sin(0.6 * x)**2 + 0.3 * np.cos(0.3 * x)**2) * 
                          np.sin(0.5 * x) * np.cos(0.2 * x) * 
                          (1 + 0.05 * np.cos(2.0 * x)))
        
        # Enhanced radial symmetry with polynomial scaling, logarithmic modulation, and chaotic oscillations
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.15 * r_squared) * (1 + 0.2 * r_squared**2) * np.log(1 + 0.03 * r_squared) * 
                     (1 + 0.1 * np.sin(4.0 * np.sqrt(r_squared)))
        
        # Cross-dimensional coupling with chaotic sine-cosine interactions, dynamic coupling coefficients, and additional modulation
        cross_term = np.sum(np.sin(x[:-1] * x[1:] * 0.5) * np.cos(x[:-1] + x[1:] * 0.3) * 
                           np.sin(0.4 * x[:-1]) * np.cos(0.1 * x[1:]) * 
                           (1 + 0.1 * np.abs(x[:-1] - x[1:])) * 
                           np.exp(-0.02 * (x[:-1]**2 + x[1:]**2)))
        
        # Additional chaotic high-frequency oscillation for extreme multimodality with dynamic scaling and feedback-based adjustment
        high_freq_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * np.sin(4.0 * x) * np.cos(3.0 * x) * 
                               (1 + 0.2 * np.sin(2.0 * x)) * 
                               (1 + 0.05 * np.cos(0.5 * x)))
        
        # Improved modulation term with enhanced feedback-based scoring and convergence properties
        mod_term = np.sum(np.sin(0.8 * x)**2 * np.cos(0.6 * x)**2 * np.sin(0.4 * x) * 
                         np.cos(0.3 * x) * np.exp(-0.05 * x**2) * 
                         (1 + 0.1 * np.sin(1.0 * x)))
        
        # Combined function with refined weights and improved convergence characteristics
        return 0.3 * exp_term + 0.25 * trig_term + 0.2 * radial_term + 0.15 * cross_term + 0.08 * high_freq_term + 0.02 * mod_term