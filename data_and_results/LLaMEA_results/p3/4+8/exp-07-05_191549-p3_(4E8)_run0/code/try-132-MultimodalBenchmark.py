import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos with higher-order terms and mixed interactions
        poly_chaos = np.sum((x_norm**4 - 1)**3 + 0.4 * (x_norm**5 - x_norm**3)**2)
        
        # Adaptive radial symmetry with dynamic frequency modulation
        radial_sym = np.sum((np.linalg.norm(x_norm, axis=0) + 0.05) * 
                           np.sin(10 * np.pi * np.linalg.norm(x_norm, axis=0)) * 
                           np.cos(7 * np.pi * np.linalg.norm(x_norm, axis=0)))
        
        # Complex trigonometric interference with multiple phase couplings
        trig_interf = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                            np.sin(8 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                            np.exp(-0.3 * x_norm**2))
        
        # Mixed exponential and polynomial barrier with variable scaling
        barrier = np.sum(np.exp(-2.5 * x_norm**2) * (x_norm**5 + 0.6 * x_norm**3 + 0.2 * x_norm))
        
        # Non-separable coupling term with chaotic modulation
        coupling = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                         np.exp(-0.7 * x_norm**2) * (x_norm**4 + 0.3 * x_norm**2 + 0.1))
        
        # Asymmetric Gaussian peaks with dynamic widths and heights
        gaussian_peaks = np.sum(0.6 * np.exp(-2.5 * (x_norm - 0.2)**2) + 
                               0.4 * np.exp(-1.8 * (x_norm + 0.5)**2) + 
                               0.3 * np.exp(-3.5 * (x_norm - 0.7)**2) + 
                               0.2 * np.exp(-2.0 * (x_norm + 0.3)**2))
        
        # Combined objective with optimized weights and additional chaotic component
        return 0.3 * poly_chaos + 0.25 * radial_sym + 0.18 * trig_interf + 0.15 * barrier + 0.12 * coupling + 0.08 * gaussian_peaks