import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(2.0 * x)**2)
        
        # Modified trigonometric couplings with radial symmetry
        radial_sym = np.sum(x**2)
        trig_coupling = np.sum(np.cos(1.5 * x) * np.sin(0.7 * x) * np.exp(-0.1 * radial_sym))
        
        # Augmented cross-term interactions with logarithmic scaling
        if self.dim > 1:
            cross_term = np.sum(np.log(1.0 + np.abs(x[:-1])) * np.log(1.0 + np.abs(x[1:])) * (x[:-1]**3 + x[1:]**3))
        else:
            cross_term = 0.0
            
        # Radial symmetry with logarithmic scaling
        log_radial = np.sum(np.log(1.0 + 0.1 * radial_sym))
        
        # Combined function with adjusted weights for better challenge
        return 0.4 * exp_term + 0.3 * trig_coupling + 0.2 * cross_term + 0.1 * log_radial