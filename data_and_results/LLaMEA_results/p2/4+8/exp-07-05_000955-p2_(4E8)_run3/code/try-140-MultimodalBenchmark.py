import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial interaction
        r = np.sqrt(np.sum(x**2))
        exp_decay = np.sum(np.exp(-0.3 * r) * np.sin(2.0 * r))
        
        # Trigonometric wave interference with varying frequencies
        wave_interference = np.sum(np.sin(3.0 * x) * np.cos(4.0 * x) * np.sin(5.0 * x))
        
        # Adaptive radial basis with multiple peaks
        rb_func = np.sum(np.exp(-0.5 * (x**2 + 0.1 * x**4)) * np.cos(6.0 * x))
        
        # Cross-dimensional coupling with polynomial interaction
        poly_coupling = np.sum((x**3 + 0.5 * x**4 + 0.2 * x**5) * np.sin(2.0 * x))
        
        # Sine-wave modulation with quadratic decay
        modulated_sine = np.sum(np.sin(1.5 * x) * np.exp(-0.2 * x**2))
        
        # Hyperbolic tangent with polynomial scaling
        tanh_poly = np.sum(np.tanh(x) * (x**2 + 0.3 * x**3))
        
        # Multi-scale Gaussian peaks with varying widths
        gaussian_peaks = np.sum(np.exp(-0.1 * (x**2 + 0.05 * x**4)) * np.cos(3.0 * x))
        
        # Combined fitness function with weighted components
        return 0.15 * exp_decay + 0.2 * wave_interference + 0.18 * rb_func + \
               0.12 * poly_coupling + 0.1 * modulated_sine + 0.15 * tanh_poly + \
               0.1 * gaussian_peaks