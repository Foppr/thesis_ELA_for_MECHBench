import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic sine-wave modulation with fractal-like terrain
        chaotic_mod = np.sum(np.sin(15 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                            np.sin(3 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm))
        
        # Radial gradient field with adaptive scaling
        radial_grad = np.sum((np.linalg.norm(x_norm, axis=0) + 0.05) * 
                           np.cos(10 * np.pi * np.linalg.norm(x_norm, axis=0)) * 
                           np.sin(6 * np.pi * np.linalg.norm(x_norm, axis=0)))
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian_peaks = np.sum(0.6 * np.exp(-2.5 * (x_norm - 0.2)**2) + 
                               0.4 * np.exp(-1.8 * (x_norm + 0.5)**2) + 
                               0.3 * np.exp(-3.2 * (x_norm - 0.7)**2) + 
                               0.2 * np.exp(-2.0 * (x_norm + 0.1)**2))
        
        # Mixed exponential-barrier terms with non-separable interaction
        barrier = np.sum(np.exp(-4.0 * x_norm**2) * (x_norm**5 + 0.4 * x_norm**3 + 0.2 * x_norm**2 + 0.1))
        
        # Trigonometric interference pattern with adaptive conditioning
        trig_interf = np.sum(np.cos(13 * np.pi * x_norm) * np.sin(9 * np.pi * x_norm) * 
                            np.cos(5 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Coupling term with polynomial chaos and radial symmetry
        coupling = np.sum(np.exp(-0.3 * x_norm**2) * (x_norm**4 + 0.3 * x_norm**2 + 0.1) * 
                         np.cos(8 * np.pi * np.linalg.norm(x_norm, axis=0)))
        
        # Combined objective with weighted components
        return 0.2 * chaotic_mod + 0.25 * radial_grad + 0.15 * gaussian_peaks + 0.15 * barrier + 0.1 * trig_interf + 0.15 * coupling