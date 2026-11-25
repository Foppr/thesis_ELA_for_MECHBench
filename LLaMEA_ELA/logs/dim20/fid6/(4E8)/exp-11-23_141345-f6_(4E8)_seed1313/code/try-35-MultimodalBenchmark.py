import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths
        rb_term = np.sum(np.exp(-0.5 * (x**2) / (1.0 + 0.1 * np.abs(x))))
        
        # Fractional polynomial terms with non-integer exponents
        frac_poly = np.sum(np.abs(x)**1.7 + 0.5 * np.abs(x)**2.3)
        
        # Asymmetric cross-term interactions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2) * (x[i+1]**1.5) + 0.3 * (x[i]**1.5) * (x[i+1]**2)
        
        # Additional sinusoidal modulation based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        modulator = 1.0 + 0.3 * np.sin(0.4 * dist_from_origin)
        
        return modulator * (0.8 * rb_term + 0.4 * frac_poly + 0.2 * cross_term)