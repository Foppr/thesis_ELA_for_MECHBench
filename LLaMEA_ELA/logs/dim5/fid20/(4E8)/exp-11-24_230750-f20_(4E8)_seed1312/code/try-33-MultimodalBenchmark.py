import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with adaptive coefficients
        exp_terms = np.sum(np.exp(-0.4 * np.abs(x)) * np.cos(2.5 * x))
        
        # Trigonometric interactions with multiple frequencies and phase shifts
        trig_terms = np.sum(np.sin(4.5 * x + 1.0) * np.cos(3.5 * x - 0.5) + 
                           np.sin(2.5 * x + 0.8) * np.cos(5.5 * x - 1.2))
        
        # Adaptive polynomial cross-terms with varying exponents and coefficients
        poly_cross = 0.07 * np.sum(x[:-1]**3 * x[1:]**3 + x[:-1]**3 * x[1:]**3)
        
        # Additional harmonic terms with increased frequency and amplitude
        harmonic_terms = 0.15 * np.sum(np.sin(7.0 * x) + np.cos(8.0 * x))
        
        # Chaotic modulation term to increase landscape ruggedness
        chaotic_mod = 0.2 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Combined function value
        return exp_terms + trig_terms + poly_cross + harmonic_terms + chaotic_mod