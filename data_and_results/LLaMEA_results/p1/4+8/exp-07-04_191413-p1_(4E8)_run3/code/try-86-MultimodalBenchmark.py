import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with varying exponents
        poly_term = np.sum((x_scaled**4 + 0.5 * x_scaled**3 + 0.2 * x_scaled**2) * (1 + 0.1 * np.abs(x_scaled)))
        
        # Gaussian peaks with dynamic centers and widths
        centers = np.linspace(-1, 1, self.dim)
        gaussian_peaks = np.sum(np.exp(-5 * (x_scaled - centers)**2) * (1 + 0.3 * np.sin(10 * x_scaled)))
        
        # Logarithmic barrier terms to prevent boundary escape
        log_barrier = np.sum(np.log(1 + 10 * (5.0 - np.abs(x_scaled))**2))
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0.5 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * (1 + 0.2 * np.abs(x_scaled[:-1] - x_scaled[1:])))
        
        # Sine-wave modulation with varying frequencies
        sine_mod = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Adaptive conditioning based on dimensionality
        conditioning = 0.3 * np.sum(x_scaled**2 * (1 + 0.1 * self.dim))
        
        # Combine all terms with different weights
        return poly_term + 0.8 * gaussian_peaks + 0.2 * log_barrier + coupling + 0.1 * sine_mod + conditioning