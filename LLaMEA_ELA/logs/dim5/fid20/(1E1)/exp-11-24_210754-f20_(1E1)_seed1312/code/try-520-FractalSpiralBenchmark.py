import numpy as np

class FractalSpiralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with logarithmic spiral modulation
        r = np.sqrt(np.sum(x**2))
        spiral_term = np.sin(10 * r) * np.cos(8 * r) * np.exp(-0.1 * r)
        
        # Multi-scale sinusoidal modulations with varying frequencies
        freq_mod = 0.5 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * 
                               np.sin(9.0 * x) * np.cos(6.0 * x))
        
        # Radial basis function with exponential decay
        rbfs = 0.3 * np.sum(np.exp(-0.5 * (x**2 + 1.0)) * np.sin(20.0 * x))
        
        # Cross-dimensional interaction with spiral coupling
        cross_dim = 0.25 * np.sum(np.sin(x[:-1] * x[1:]) * 
                                 np.cos(0.5 * x[:-1] + 1.5 * x[1:]))
        
        # Fractal-like structure with recursive scaling
        fractal = 0.2 * np.sum(np.sin(25.0 * np.sin(3.0 * x)) * 
                              np.cos(20.0 * np.cos(4.0 * x)))
        
        # Asymmetric polynomial with exponential weighting
        asym_poly = 0.18 * np.sum((x**3.5 + 0.7 * x**2.8 - 0.3 * x) * 
                                 np.exp(-0.2 * np.abs(x)))
        
        # Multi-scale harmonic modulation with phase shifts
        harmonic = 0.15 * np.sum(np.sin(30.0 * x + np.sin(10.0 * x)) * 
                                np.cos(25.0 * x + np.cos(8.0 * x)))
        
        # Sharp gradient components with chaotic coupling
        sharp_gradients = 0.22 * np.sum(np.sin(40.0 * x) * 
                                       np.cos(35.0 * x) * 
                                       np.exp(-0.1 * np.abs(x)))
        
        # Combined fractal spiral structure
        return (spiral_term + freq_mod + rbfs + cross_dim + 
                fractal + asym_poly + harmonic + sharp_gradients)