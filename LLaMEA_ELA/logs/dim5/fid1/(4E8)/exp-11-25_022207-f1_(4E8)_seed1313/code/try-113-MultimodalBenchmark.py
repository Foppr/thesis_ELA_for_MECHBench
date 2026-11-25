import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle point structure with exponential coupling
        chaotic_term = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.pi * x_norm) * 
                             np.cos(2 * np.pi * x_norm) * 
                             (1 + 0.3 * np.sin(3 * x_norm)))
        
        # Fractal-like gradient variations using fractional Brownian motion approximations
        fractal_term = np.sum((x_norm**2 + 0.1) * 
                             np.sin(10 * np.pi * x_norm) * 
                             np.cos(5 * np.pi * x_norm) * 
                             np.exp(-0.5 * x_norm**2))
        
        # Exponential coupling with asymmetric repulsion
        coupling_term = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                              (x_norm[:-1] - x_norm[1:])**3 * 
                              np.sin(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Multi-scale harmonic modulation with varying frequencies
        multi_scale = np.sum(np.sin(2 * np.pi * x_norm) * 
                            np.cos(4 * np.pi * x_norm) * 
                            np.sin(8 * np.pi * x_norm) * 
                            (1 + 0.2 * np.cos(6 * np.pi * x_norm)))
        
        # Asymmetric polynomial landscape with logarithmic perturbations
        poly_term = np.sum((x_norm**4 - 0.5 * x_norm**2 + 0.1 * x_norm) * 
                          np.log(1 + np.abs(x_norm)) * 
                          np.exp(-0.3 * x_norm**2))
        
        # Combined landscape with global conditioning
        return chaotic_term + fractal_term - coupling_term + multi_scale + poly_term