import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with higher frequency
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(3.0 * x)**3)
        
        # Modified trigonometric couplings with phase shifts
        radial_sym = np.sum(x**2)
        trig_coupling = np.sum(np.cos(2.0 * x + 0.5) * np.sin(1.2 * x - 0.3) * np.exp(-0.15 * radial_sym))
        
        # Augmented cross-term interactions with polynomial coupling
        if self.dim > 1:
            cross_term = np.sum((x[:-1]**2 + x[1:]**2) * np.sin(0.5 * (x[:-1] + x[1:]))**2)
        else:
            cross_term = 0.0
            
        # Radial symmetry with logarithmic scaling and additional quadratic term
        log_radial = np.sum(np.log(1.0 + 0.05 * radial_sym) + 0.01 * radial_sym**2)
        
        # Additional high-frequency oscillation component
        high_freq = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) * np.exp(-0.2 * radial_sym))
        
        # Combined function with adjusted weights for better challenge
        return 0.35 * exp_term + 0.3 * trig_coupling + 0.2 * cross_term + 0.1 * log_radial + 0.05 * high_freq