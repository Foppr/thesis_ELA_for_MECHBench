import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with adaptive coefficients
        exp_terms = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(2.0 * x))
        
        # Trigonometric interactions with multiple frequencies
        trig_terms = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) + np.sin(2.0 * x) * np.cos(5.0 * x))
        
        # Adaptive polynomial cross-terms with varying exponents and coefficients
        poly_cross = 0.05 * np.sum(x[:-1]**4 * x[1:]**2 + x[:-1]**2 * x[1:]**4)
        
        # Additional harmonic terms to increase complexity
        harmonic_terms = 0.1 * np.sum(np.sin(6.0 * x) + np.cos(7.0 * x))
        
        # Combined function value
        return exp_terms + trig_terms + poly_cross + harmonic_terms