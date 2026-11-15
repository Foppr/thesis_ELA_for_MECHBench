import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with varying centers and widths
        centers = np.linspace(-1, 1, self.dim)
        widths = np.linspace(0.5, 2.0, self.dim)
        rb = np.sum(np.exp(-widths * (x_norm - centers)**2))
        
        # High-frequency trigonometric terms with varying amplitudes
        freqs = np.arange(1, self.dim + 1) * 8.0
        trig = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Asymmetric penalty terms
        asym_penalty = np.sum(np.where(x_norm > 0, 
                                      10 * x_norm**2 + 2 * x_norm**4,
                                      5 * x_norm**2 + x_norm**3))
        
        # Multi-scale periodic components
        scale_factors = np.logspace(0, 2, self.dim)
        multi_scale = np.sum(np.sin(scale_factors * x_norm) * np.cos(scale_factors * x_norm))
        
        # Cross-dimensional coupling with exponential interactions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2)) * np.sin(x_norm[i] * x_norm[i+1])
        
        # Fractional power and logarithmic interactions
        frac_power = np.sum(np.abs(x_norm)**1.7)
        log_interaction = np.sum(np.log(1.1 + np.abs(x_norm)) * np.sin(x_norm))
        
        # Sine-cosine hybrid with phase modulation
        phase_mod = np.sin(2 * np.arange(self.dim) * np.pi / self.dim)
        hybrid = np.sum(np.sin(x_norm + phase_mod) * np.cos(x_norm + phase_mod))
        
        # Polynomial and exponential mix
        poly_exp = np.sum(x_norm**3 * np.exp(-0.5 * x_norm**2))
        
        # Combined result
        return rb + trig + asym_penalty + multi_scale + coupling + frac_power + log_interaction + hybrid + poly_exp