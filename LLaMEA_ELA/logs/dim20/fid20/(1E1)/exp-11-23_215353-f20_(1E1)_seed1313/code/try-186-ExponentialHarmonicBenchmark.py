import numpy as np

class ExponentialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonics component with varying degrees and orders
        sph_harm_term = 0.0
        for i in range(self.dim):
            sph_harm_term += (np.sin(x[i])**2 + np.cos(x[i])**2) * np.exp(-0.1 * x[i]**2)
        
        # Exponential decay terms with different decay rates and offsets
        exp_decay_term = np.sum(np.exp(-0.5 * (x**2)) * np.sin(2.0 * x) * np.cos(3.0 * x))
        
        # Gradient-based attraction fields creating valleys and ridges
        grad_attraction = 0.0
        for i in range(self.dim):
            grad_attraction += (x[i] - np.sin(x[i]))**2
        
        # Polynomial interpolation with non-linear coefficients
        poly_interp = np.sum((x**3 + 0.5 * x**2 - 0.3 * x + 1.0)**1.5)
        
        # Multi-scale sinusoidal modulation for fine-grained complexity
        multi_freq_term = np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.exp(-0.05 * x**2))
        
        # Cross-dimensional interaction terms with varying weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x[i] * x[i+1]) * np.sin(x[i] + x[i+1])
        
        # Radial symmetry component with peak localization
        radial_term = np.sum(np.exp(-0.2 * np.sum(x**2)) * np.cos(5.0 * np.sqrt(np.sum(x**2))))
        
        # Quadratic distortion with directional sensitivity
        quad_distort = np.sum(0.4 * (x**2) * np.cos(0.8 * x))
        
        # Global scaling and offset to control overall function range
        return 0.2 * sph_harm_term + 0.15 * exp_decay_term + 0.12 * grad_attraction + 0.13 * poly_interp + 0.11 * multi_freq_term + 0.08 * cross_interaction + 0.09 * radial_term + 0.07 * quad_distort + 1.5