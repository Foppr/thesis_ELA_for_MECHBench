import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum((x_norm**2 - 1)**4 + 0.3 * (x_norm**3 - x_norm)**2)
        
        # Radial symmetry with varying harmonic frequencies
        radial_sym = np.sum((np.linalg.norm(x_norm, axis=0) + 0.1) * 
                           np.sin(9 * np.pi * np.linalg.norm(x_norm, axis=0)) * 
                           np.cos(6 * np.pi * np.linalg.norm(x_norm, axis=0)))
        
        # Trigonometric interference pattern with phase modulation
        trig_interf = np.sum(np.sin(13 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * 
                            np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Mixed exponential and polynomial barrier with adaptive scaling
        barrier = np.sum(np.exp(-2.5 * x_norm**2) * (x_norm**4 + 0.6 * x_norm**2 + 0.12))
        
        # Coupling term with non-separable interaction
        coupling = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                         np.exp(-0.4 * x_norm**2) * (x_norm**3 + 0.25 * x_norm))
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian_peaks = np.sum(0.6 * np.exp(-2.2 * (x_norm - 0.3)**2) + 
                               0.4 * np.exp(-1.7 * (x_norm + 0.4)**2) + 
                               0.3 * np.exp(-3.2 * (x_norm - 0.6)**2))
        
        # Combined objective with weighted components
        return 0.27 * poly_chaos + 0.18 * radial_sym + 0.17 * trig_interf + 0.18 * barrier + 0.08 * coupling + 0.12 * gaussian_peaks