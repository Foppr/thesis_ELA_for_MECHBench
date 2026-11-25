import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with sine-modulated coefficients
        exp_term = np.sum(np.exp(-0.2 * x**2) * np.sin(0.2 * x)**3)
        
        # Nested sinusoidal couplings with varying phase shifts and amplitudes
        trig_term = np.sum(np.sin(0.8 * x + 0.1 * np.sin(0.5 * x)) * 
                          np.cos(0.4 * x + 0.2 * np.cos(0.3 * x)) * 
                          np.sin(0.1 * x + 0.3 * np.sin(0.7 * x)))
        
        # Adaptive radial symmetry with polynomial barrier and log-scaling
        r_squared = np.sum(x**2)
        radial_term = (r_squared + 0.5) * np.exp(-0.1 * r_squared) * np.log(1 + 0.2 * r_squared + 0.01 * r_squared**2)
        
        # Cross-dimensional coupling with chaotic polynomial interactions
        cross_term = np.sum(x[:-1]**3 * x[1:]**2 * np.sin(0.4 * x[:-1] + 0.3 * x[1:]) * 
                           np.cos(0.2 * x[:-1] - 0.5 * x[1:]))
        
        # Additional chaotic harmonic term for increased multimodality
        harm_term = np.sum(np.sin(1.2 * x) * np.cos(0.9 * x) * np.sin(0.6 * x) * np.cos(0.3 * x))
        
        # Combined function with dynamically adjusted weights
        return 0.3 * exp_term + 0.4 * trig_term + 0.2 * radial_term + 0.05 * cross_term + 0.05 * harm_term