import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multiple exponential decay terms with different rates
        exp_terms = np.sum(np.exp(-0.3 * x**2) + 0.5 * np.exp(-0.7 * x**2))
        
        # Enhanced trigonometric interactions with multiple frequencies
        trig_terms = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) + 0.3 * np.sin(7.0 * x) * np.cos(6.0 * x))
        
        # Complex polynomial cross-terms with higher exponents and interaction coefficients
        poly_cross = 0.2 * np.sum(x[:-2]**4 * x[1:-1]**3 * x[2:])
        
        # Additional sinusoidal modulation to increase landscape complexity
        modulate = np.sum(0.4 * np.sin(10.0 * x) * np.cos(9.0 * x))
        
        # Ruggedness term using step functions and noise-like behavior
        ruggedness = 0.1 * np.sum(np.abs(np.sin(x)) * np.cos(2.0 * x))
        
        # Combined function value
        return exp_terms + trig_terms + poly_cross + modulate + ruggedness