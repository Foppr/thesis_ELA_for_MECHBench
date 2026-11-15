import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial conditioning term
        poly_cond = np.sum(x_scaled**4)
        
        # Gaussian peaks with varying heights and widths
        peaks = 0.0
        for i in range(1, 6):
            peak_height = 1.0 / i
            peak_width = 0.5 / i
            peak_center = np.array([np.sin(i) * 0.5] * self.dim)
            peak = peak_height * np.exp(-np.sum(((x_scaled - peak_center) / peak_width)**2))
            peaks += peak
            
        # Logarithmic barrier terms to prevent boundary escape
        barriers = 0.0
        for i in range(self.dim):
            barriers += -np.log(1.0 - (x_scaled[i] + 1.0)**2) - np.log(1.0 - (1.0 - x_scaled[i])**2)
            
        # Chaotic sine modulation with varying frequencies
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.sin(15 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.5 * poly_cond + 2.0 * peaks + 0.3 * barriers + 0.1 * chaotic