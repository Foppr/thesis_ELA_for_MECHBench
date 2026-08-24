import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos with higher-order terms and mixed interactions
        poly_chaos = np.sum((x_norm**2 - 1)**5 + 0.4 * (x_norm**4 - x_norm**2)**2 + 0.2 * (x_norm**3 - x_norm)**3)
        
        # Adaptive radial symmetry with chaotic frequency modulation
        radial_sym = np.sum((np.linalg.norm(x_norm, axis=0) + 0.05) * 
                           np.sin(10 * np.pi * np.linalg.norm(x_norm, axis=0) + 
                                  2 * np.sin(3 * np.pi * np.linalg.norm(x_norm, axis=0))) * 
                           np.cos(7 * np.pi * np.linalg.norm(x_norm, axis=0) + 
                                  1.5 * np.cos(2 * np.pi * np.linalg.norm(x_norm, axis=0))))
        
        # Trigonometric interference with chaotic phase modulation and mixed harmonics
        trig_interf = np.sum(np.sin(15 * np.pi * x_norm + 0.5 * np.sin(5 * np.pi * x_norm)) * 
                            np.cos(12 * np.pi * x_norm + 0.3 * np.cos(4 * np.pi * x_norm)) * 
                            np.sin(9 * np.pi * x_norm + 0.4 * np.sin(3 * np.pi * x_norm)) * 
                            np.cos(6 * np.pi * x_norm + 0.2 * np.cos(2 * np.pi * x_norm)))
        
        # Mixed exponential and polynomial barrier with adaptive scaling and chaotic modulation
        barrier = np.sum(np.exp(-4.0 * x_norm**2) * (x_norm**5 + 0.6 * x_norm**3 + 0.2 * x_norm**2 + 0.1) + 
                        0.1 * np.exp(-2.0 * x_norm**2) * np.sin(8 * np.pi * x_norm))
        
        # Coupling term with non-separable interaction and chaotic modulation
        coupling = np.sum(np.sin(9 * np.pi * x_norm + 0.3 * np.sin(3 * np.pi * x_norm)) * 
                         np.cos(6 * np.pi * x_norm + 0.2 * np.cos(2 * np.pi * x_norm)) * 
                         np.exp(-0.7 * x_norm**2) * (x_norm**4 + 0.3 * x_norm**2 + 0.1))
        
        # Asymmetric Gaussian peaks with chaotic positioning and varying widths
        gaussian_peaks = np.sum(0.6 * np.exp(-2.5 * (x_norm - 0.25)**2 + 0.1 * np.sin(5 * np.pi * x_norm)) + 
                               0.4 * np.exp(-1.8 * (x_norm + 0.35)**2 + 0.15 * np.cos(4 * np.pi * x_norm)) + 
                               0.3 * np.exp(-3.2 * (x_norm - 0.55)**2 + 0.1 * np.sin(6 * np.pi * x_norm)))
        
        # Combined objective with optimized weights and chaotic modulation
        return 0.3 * poly_chaos + 0.25 * radial_sym + 0.2 * trig_interf + 0.15 * barrier + 0.1 * coupling + 0.05 * gaussian_peaks