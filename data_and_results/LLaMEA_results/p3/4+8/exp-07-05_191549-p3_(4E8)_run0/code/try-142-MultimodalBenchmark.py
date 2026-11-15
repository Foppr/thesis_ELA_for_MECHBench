import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos with higher-order terms and mixed interactions
        poly_chaos = np.sum((x_norm**6 - 2*x_norm**4 + x_norm**2)**2 + 
                           0.2 * (x_norm**5 - x_norm**3)**2 + 
                           0.1 * (x_norm**4 - x_norm**2)**3)
        
        # Adaptive radial symmetry with chaotic frequency modulation
        r = np.linalg.norm(x_norm, axis=0)
        radial_sym = np.sum((r + 0.05) * 
                           np.sin(12 * np.pi * r + 2 * np.sin(24 * np.pi * r)) * 
                           np.cos(8 * np.pi * r + 3 * np.cos(18 * np.pi * r)))
        
        # Trigonometric interference with chaotic phase modulation and mixed frequencies
        trig_interf = np.sum(np.sin(18 * np.pi * x_norm + 0.5 * np.sin(36 * np.pi * x_norm)) * 
                            np.cos(14 * np.pi * x_norm + 0.3 * np.cos(28 * np.pi * x_norm)) * 
                            np.sin(10 * np.pi * x_norm + 0.4 * np.sin(20 * np.pi * x_norm)) * 
                            np.cos(7 * np.pi * x_norm + 0.2 * np.cos(14 * np.pi * x_norm)))
        
        # Mixed exponential and polynomial barrier with adaptive scaling and chaotic modulation
        barrier = np.sum(np.exp(-2.8 * x_norm**2) * (x_norm**6 + 0.45 * x_norm**4 + 0.22 * x_norm**2 + 0.06) + 
                        0.12 * np.exp(-1.2 * x_norm**2) * np.sin(22 * np.pi * x_norm)**2)
        
        # Coupling term with non-separable interaction and chaotic modulation
        coupling = np.sum(np.sin(9 * np.pi * x_norm + 0.3 * np.sin(18 * np.pi * x_norm)) * 
                         np.cos(6 * np.pi * x_norm + 0.2 * np.cos(12 * np.pi * x_norm)) * 
                         np.exp(-0.35 * x_norm**2) * (x_norm**4 + 0.32 * x_norm**2 + 0.06))
        
        # Asymmetric Gaussian peaks with chaotic positioning and varying widths
        gaussian_peaks = np.sum(0.65 * np.exp(-2.7 * (x_norm - 0.27)**2 + 0.11 * np.sin(22 * np.pi * x_norm)) + 
                               0.42 * np.exp(-2.0 * (x_norm + 0.37)**2 + 0.16 * np.cos(17 * np.pi * x_norm)) + 
                               0.32 * np.exp(-3.4 * (x_norm - 0.57)**2 + 0.11 * np.sin(27 * np.pi * x_norm)))
        
        # Combined objective with optimized weights for better conditioning
        return 0.21 * poly_chaos + 0.19 * radial_sym + 0.16 * trig_interf + 0.19 * barrier + 0.13 * coupling + 0.16 * gaussian_peaks