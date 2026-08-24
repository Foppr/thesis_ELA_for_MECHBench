import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like recursive sine-wave modulation
        fractal_term = np.sum(np.sin(2**6 * np.pi * x_scaled) * np.sin(2**5 * np.pi * x_scaled) * 
                             np.sin(2**4 * np.pi * x_scaled) * np.sin(2**3 * np.pi * x_scaled) * 
                             np.sin(2**2 * np.pi * x_scaled) * np.sin(2**1 * np.pi * x_scaled))
        
        # Radial gradient field with varying intensity
        radial_grad = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.2) * 
                            np.cos(8 * np.pi * x_scaled) * np.sin(6 * np.pi * x_scaled))
        
        # Asymmetric Gaussian peaks with varying heights and widths
        gaussian_term = np.sum(np.exp(-2.0 * (x_scaled - 0.3)**2) * np.exp(-1.5 * (x_scaled + 0.4)**2) * 
                              (np.sin(12 * np.pi * x_scaled)**2 + 0.5 * np.cos(10 * np.pi * x_scaled)**2))
        
        # Non-separable interaction terms with high conditioning
        interaction_term = np.sum((x_scaled[:-1] + x_scaled[1:])**4 + 
                                 (x_scaled[:-1] - x_scaled[1:])**3 + 
                                 np.sin(5 * np.pi * x_scaled[:-1]) * np.cos(5 * np.pi * x_scaled[1:]))
        
        # Multi-scale harmonic interference
        harmonic_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled) * 
                              np.sin(5 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Combined weighted landscape
        return 0.25 * fractal_term + 0.2 * radial_grad + 0.25 * gaussian_term + 0.15 * interaction_term + 0.15 * harmonic_term