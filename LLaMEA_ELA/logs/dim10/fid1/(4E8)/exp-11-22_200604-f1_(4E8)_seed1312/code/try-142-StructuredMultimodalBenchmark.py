import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Radial basis function component with varying widths
        rb_weights = 1.0 + 0.5 * np.sin(2 * np.pi * x_norm)
        rb_centers = np.linspace(-1, 1, self.dim)
        rb_sum = np.sum(rb_weights * np.exp(-10 * (x_norm - rb_centers)**2))
        f2 = 0.5 * rb_sum
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        freqs = 1 + 2 * np.abs(x_norm)
        amp = 1.5 + 0.5 * np.cos(3 * x_norm)
        f3 = 0.3 * np.sum(amp * np.sin(freqs * np.pi * x_norm))
        
        # Asymmetric hyperbolic penalty terms
        f4 = 0.4 * np.sum(np.abs(x_norm) / (1 + np.exp(-5 * x_norm)))
        
        # Cross-dimensional coupling with trigonometric interactions
        coupling = 0.2 * np.sum(np.sin(10 * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(8 * (x_norm[:-1] - x_norm[1:])))
        f5 = coupling
        
        # Multi-scale harmonic oscillations
        f6 = 0.25 * np.sum(np.sin(20 * x_norm**2) * np.cos(15 * x_norm**3))
        
        # Gaussian-like peaks with dynamic positioning
        peak_positions = 0.3 * np.sin(4 * x_norm)
        f7 = 0.3 * np.sum(np.exp(-0.5 * ((x_norm - peak_positions) / 0.5)**2))
        
        # Asymmetric saddle-like regions
        f8 = 0.2 * np.sum(x_norm**3 * np.sin(5 * x_norm))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
        
        return result