import numpy as np

class SinusoidalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic sinusoidal terms with varying frequencies and amplitudes
        f1 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                   np.exp(-0.5 * x_norm**2))
        
        # Polynomial conditioning with dimensionality-dependent exponents
        poly_exponent = 1.5 + 0.3 * np.log(self.dim + 1)
        f2 = np.sum(np.abs(x_norm)**poly_exponent * np.sin(4 * x_norm) * 
                   np.cos(2 * x_norm))
        
        # Cross-dimensional coupling with polynomial interactions
        f3 = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                   np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Multi-scale periodic modulation with chaotic frequency variations
        freq_mod = 1.0 + 0.5 * np.sin(self.dim * 0.7) + 0.3 * np.cos(self.dim * 0.4)
        f4 = np.sum(np.sin(freq_mod * np.pi * x_norm**1.2) * 
                   np.cos(freq_mod * np.pi * x_norm**0.8) * 
                   np.exp(-0.4 * np.abs(x_norm)**1.5))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * 0.3)
        
        # Combine all components with different weights
        result = (f1 + 0.7 * f2 + 0.6 * f3 + 0.8 * f4) * condition_factor
        
        # Add small random noise for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise