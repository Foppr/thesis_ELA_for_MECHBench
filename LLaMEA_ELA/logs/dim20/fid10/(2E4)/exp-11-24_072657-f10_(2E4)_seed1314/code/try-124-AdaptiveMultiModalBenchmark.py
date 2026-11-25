import numpy as np

class AdaptiveMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial landscape with varying degrees
        poly_term = np.sum((x_norm**2 + 0.3 * x_norm**4 + 0.05 * x_norm**6)**2)
        
        # Trigonometric oscillations with adaptive frequencies
        freqs = 2.5 + 1.5 * np.sin(np.arange(self.dim) * 0.7)
        trig_term = np.sum(np.cos(freqs * np.pi * x_norm) * np.sin(freqs * np.pi * x_norm**2))
        
        # Radial basis function components with adaptive widths
        rb_widths = 0.5 + 0.3 * np.log(self.dim + 1)
        rb_centers = np.linspace(-1, 1, self.dim)
        rb_term = np.sum(np.exp(-rb_widths * (x_norm - rb_centers)**2))
        
        # Cross-dimensional interaction terms with adaptive coupling
        coupling_strength = 0.8 + 0.2 * np.log(self.dim + 1)
        cross_term = np.sum(coupling_strength * x_norm[:-1] * x_norm[1:] * 
                           np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.2 + 0.3 * np.log(self.dim + 1) + 0.1 * np.cos(self.dim * 0.5)
        
        # Combined landscape with multi-modal characteristics
        result = (poly_term + 0.6 * trig_term + 0.4 * rb_term + 0.3 * cross_term) * condition_factor
        
        # Add chaotic noise component for increased complexity
        noise = 0.005 * np.random.random() * np.sin(self.dim * 1.2)
        
        return result + noise