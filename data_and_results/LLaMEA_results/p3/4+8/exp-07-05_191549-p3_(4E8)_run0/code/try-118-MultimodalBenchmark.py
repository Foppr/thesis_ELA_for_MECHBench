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
                           np.sin(10 * np.pi * r + 2 * np.sin(20 * np.pi * r)) * 
                           np.cos(7 * np.pi * r + 3 * np.cos(15 * np.pi * r)))
        
        # Trigonometric interference with chaotic phase modulation and mixed frequencies
        trig_interf = np.sum(np.sin(15 * np.pi * x_norm + 0.5 * np.sin(30 * np.pi * x_norm)) * 
                            np.cos(12 * np.pi * x_norm + 0.3 * np.cos(25 * np.pi * x_norm)) * 
                            np.sin(9 * np.pi * x_norm + 0.4 * np.sin(18 * np.pi * x_norm)) * 
                            np.cos(6 * np.pi * x_norm + 0.2 * np.cos(12 * np.pi * x_norm)))
        
        # Mixed exponential and polynomial barrier with adaptive scaling and chaotic modulation
        barrier = np.sum(np.exp(-2.5 * x_norm**2) * (x_norm**6 + 0.4 * x_norm**4 + 0.2 * x_norm**2 + 0.05) + 
                        0.1 * np.exp(-x_norm**2) * np.sin(20 * np.pi * x_norm)**2)
        
        # Coupling term with non-separable interaction and chaotic modulation
        coupling = np.sum(np.sin(8 * np.pi * x_norm + 0.3 * np.sin(16 * np.pi * x_norm)) * 
                         np.cos(5 * np.pi * x_norm + 0.2 * np.cos(10 * np.pi * x_norm)) * 
                         np.exp(-0.3 * x_norm**2) * (x_norm**4 + 0.3 * x_norm**2 + 0.05))
        
        # Asymmetric Gaussian peaks with chaotic positioning and varying widths
        gaussian_peaks = np.sum(0.6 * np.exp(-2.5 * (x_norm - 0.25)**2 + 0.1 * np.sin(20 * np.pi * x_norm)) + 
                               0.4 * np.exp(-1.8 * (x_norm + 0.35)**2 + 0.15 * np.cos(15 * np.pi * x_norm)) + 
                               0.3 * np.exp(-3.2 * (x_norm - 0.55)**2 + 0.1 * np.sin(25 * np.pi * x_norm)))
        
        # Combined objective with optimized weights for better conditioning
        return 0.2 * poly_chaos + 0.18 * radial_sym + 0.15 * trig_interf + 0.18 * barrier + 0.12 * coupling + 0.17 * gaussian_peaks