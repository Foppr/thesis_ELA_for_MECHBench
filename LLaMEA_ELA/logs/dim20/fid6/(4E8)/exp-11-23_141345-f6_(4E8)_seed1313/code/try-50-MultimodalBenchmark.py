import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with stronger attenuation and additional modulation
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.cos(0.5 * x))
        
        # Modified trigonometric coupling with higher frequencies, phase shifts, and interaction terms
        trig_term = np.sum(np.sin(1.2 * x) * np.cos(0.8 * x) * np.sin(0.4 * x) * np.cos(0.2 * x))
        
        # Augmented radial symmetry with quartic scaling and cross-dimensional coupling
        radial_term = np.sum(x**4 * np.exp(-0.15 * np.sum(x**2)))
        
        # Cross-dimensional interaction terms to increase complexity and challenge convergence
        cross_term = np.sum((x[:-1] - x[1:])**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Combined function with updated weights for increased complexity and better fitness score
        return 0.25 * exp_term + 0.35 * trig_term + 0.3 * radial_term + 0.1 * cross_term