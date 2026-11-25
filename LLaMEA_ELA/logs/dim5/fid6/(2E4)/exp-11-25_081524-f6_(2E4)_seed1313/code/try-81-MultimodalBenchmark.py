import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        rb_centers = np.linspace(-4, 4, min(5, self.dim))
        rb_widths = 0.5 + 0.5 * np.random.rand(min(5, self.dim))
        rb_sum = 0.0
        for i in range(min(5, self.dim)):
            rb_sum += np.exp(-rb_widths[i] * np.sum((x - rb_centers[i])**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * (1.0 + 0.3 * np.sin(x)))
        
        # Asymmetric saddle points with exponential decay
        saddle_terms = 0.0
        for i in range(self.dim - 1):
            saddle_terms += (x[i]**2 - x[i+1]**2)**2 * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Cross-dimensional polynomial interactions with mixed signs
        poly_cross = 0.0
        for i in range(self.dim - 2):
            poly_cross += (x[i] * x[i+1] * x[i+2])**2 + 0.5 * (x[i]**3 + x[i+1]**3)
        
        # Chaotic scaling factor based on cumulative sum
        chaotic_scale = 1.0 + 0.2 * np.sin(np.sum(x) * 0.7)
        
        # Combined fitness with conditioning
        result = chaotic_scale * (np.sum(x**4) + 0.5 * sin_modulation + rb_sum + saddle_terms + poly_cross)
        
        return result