import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic fractal scaling with nested harmonic patterns
        log_term = np.sum(np.log(np.abs(x) + 1.0) * np.sin(np.log(np.abs(x) + 1.0)))
        
        # Multi-resolution harmonic interference with varying frequencies
        harm_interference = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(0.5 * x) * 
                                  np.cos(1.5 * x) * np.sin(0.2 * x))
        
        # Self-similar fractal structure with recursive scaling
        fractal_term = np.sum(np.power(np.abs(x), 1.3 + 0.2 * np.sin(4.0 * x)) * 
                             np.cos(2.0 * np.log(np.abs(x) + 1.0)))
        
        # Nested valley structure with exponential modulation
        valley_term = np.sum(np.exp(-0.5 * (x**2 - 1.0)**2) * 
                            np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Multi-scale coupling with asymmetric interaction weights
        coupling_term = np.sum((x[:-1]**3 + x[1:]**3) * np.sin(1.2 * x[:-1]) * 
                              np.cos(1.8 * x[1:]) * (1.0 + 0.1 * np.sin(2.5 * x[:-1])))
        
        # Logarithmic frequency modulation with harmonic resonance
        freq_mod_term = np.sum(np.sin(3.0 * np.log(np.abs(x) + 1.0)) * 
                              np.cos(2.0 * np.log(np.abs(x) + 1.0)) * 
                              (1.0 + 0.3 * np.cos(5.0 * x)))
        
        # Combined function with multi-fractal weighting
        return 0.25 * log_term + 0.2 * harm_interference + 0.18 * fractal_term + \
               0.15 * valley_term + 0.12 * coupling_term + 0.1 * freq_mod_term