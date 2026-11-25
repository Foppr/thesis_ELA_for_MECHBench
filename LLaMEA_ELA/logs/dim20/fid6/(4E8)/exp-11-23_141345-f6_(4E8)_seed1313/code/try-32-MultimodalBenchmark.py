import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with stronger attenuation
        exp_term = np.sum(np.exp(-0.2 * x**2))
        
        # Modified trigonometric coupling with higher frequencies and additional interaction
        trig_term = np.sum(np.cos(0.7 * x) * np.sin(0.4 * x) * np.cos(0.2 * x) * np.sin(0.1 * x))
        
        # Augmented radial symmetry with cubic scaling and cross-terms
        radial_term = np.sum(x**3 * np.exp(-0.1 * np.sum(x**2)))
        
        # Combined function with updated weights for increased complexity
        return 0.3 * exp_term + 0.4 * trig_term + 0.3 * radial_term