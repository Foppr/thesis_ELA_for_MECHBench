import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified exponential decay terms with different rates
        exp_terms = np.sum(0.7 * np.exp(-0.2 * x**2) + 0.3 * np.exp(-0.6 * x**2))
        
        # Enhanced trigonometric interactions with altered frequencies
        trig_terms = np.sum(np.sin(6.0 * x) * np.cos(3.0 * x) + 0.4 * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # New quartic polynomial cross-term for increased complexity
        poly_cross = 0.15 * np.sum(x[:-2]**4 * x[1:-1]**2 * x[2:])
        
        # Additional sinusoidal modulation with higher frequency components
        modulate = np.sum(0.5 * np.sin(12.0 * x) * np.cos(11.0 * x))
        
        # Ruggedness term using absolute value and enhanced cosine interaction
        ruggedness = 0.12 * np.sum(np.abs(np.sin(x)) * np.cos(3.0 * x))
        
        # Combined function value
        return exp_terms + trig_terms + poly_cross + modulate + ruggedness