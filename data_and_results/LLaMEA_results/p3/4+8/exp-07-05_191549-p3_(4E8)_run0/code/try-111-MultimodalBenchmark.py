import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like recursive sine-wave modulation
        fractal_term = np.sum(np.sin(32 * np.pi * x_scaled) * 
                             np.sin(16 * np.pi * x_scaled) * 
                             np.sin(8 * np.pi * x_scaled) * 
                             np.sin(4 * np.pi * x_scaled) * 
                             np.sin(2 * np.pi * x_scaled))
        
        # Radial gradient field with asymmetric Gaussian peaks
        radial_gradient = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.2) * 
                               np.exp(-x_scaled**2) * 
                               np.sin(12 * np.pi * x_scaled) * 
                               np.cos(8 * np.pi * x_scaled))
        
        # Asymmetric Gaussian peaks with varying heights and widths
        gaussian_peaks = np.sum(0.5 * np.exp(-10 * (x_scaled - 0.3)**2) + 
                               0.3 * np.exp(-5 * (x_scaled + 0.4)**2) + 
                               0.2 * np.exp(-15 * (x_scaled - 0.1)**2))
        
        # Non-separable interaction terms with chaotic modulation
        nonsep_term = np.sum(np.sin(20 * np.pi * x_scaled**3) * 
                            np.cos(15 * np.pi * x_scaled**2) * 
                            np.sin(10 * np.pi * x_scaled) * 
                            np.cos(5 * np.pi * x_scaled))
        
        # Mixed exponential-barrier and polynomial interaction
        exp_poly_term = np.sum((np.exp(-3 * x_scaled**2) + 0.1 * x_scaled**8) * 
                              (np.sin(9 * np.pi * x_scaled)**4 + 0.7 * np.cos(13 * np.pi * x_scaled)**4))
        
        # Additional sinusoidal shift for enhanced conditioning
        shift_term = np.sum(np.sin(35 * np.pi * x_scaled + 0.7 * np.pi) * 
                           np.cos(25 * np.pi * x_scaled + 0.3 * np.pi) * 
                           np.sin(15 * np.pi * x_scaled + 0.1 * np.pi))
        
        # Combine all terms with optimized weights
        return 0.25 * fractal_term + 0.2 * radial_gradient + 0.15 * gaussian_peaks + 0.15 * nonsep_term + 0.1 * exp_poly_term + 0.15 * shift_term