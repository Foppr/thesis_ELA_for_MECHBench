import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like terrain using recursive sine-wave modulation
        fractal = np.sum(np.sin(32 * np.pi * x_norm) * np.sin(16 * np.pi * x_norm) * 
                        np.sin(8 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm) * 
                        np.sin(2 * np.pi * x_norm))
        
        # Radial gradient field with chaotic modulation
        r = np.linalg.norm(x_norm, axis=0)
        radial_grad = np.sum(r * np.sin(20 * np.pi * r + 0.5 * np.sin(40 * np.pi * r)) * 
                           np.cos(15 * np.pi * r + 0.3 * np.cos(30 * np.pi * r)))
        
        # Asymmetric Gaussian peaks with varying widths and chaotic positioning
        gaussian_peaks = np.sum(0.8 * np.exp(-3.0 * (x_norm - 0.3)**2 + 0.2 * np.sin(25 * np.pi * x_norm)) + 
                               0.6 * np.exp(-2.2 * (x_norm + 0.4)**2 + 0.15 * np.cos(20 * np.pi * x_norm)) + 
                               0.4 * np.exp(-4.0 * (x_norm - 0.6)**2 + 0.1 * np.sin(30 * np.pi * x_norm)) + 
                               0.3 * np.exp(-1.5 * (x_norm + 0.2)**2 + 0.25 * np.cos(15 * np.pi * x_norm)))
        
        # Trigonometric interference with mixed frequencies and chaotic phase modulation
        trig_interf = np.sum(np.sin(25 * np.pi * x_norm + 0.4 * np.sin(50 * np.pi * x_norm)) * 
                            np.cos(20 * np.pi * x_norm + 0.3 * np.cos(40 * np.pi * x_norm)) * 
                            np.sin(15 * np.pi * x_norm + 0.2 * np.sin(30 * np.pi * x_norm)) * 
                            np.cos(10 * np.pi * x_norm + 0.1 * np.cos(20 * np.pi * x_norm)))
        
        # Mixed exponential and polynomial barrier terms with adaptive scaling
        barrier = np.sum(np.exp(-3.0 * x_norm**2) * (x_norm**5 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.1) + 
                        0.2 * np.exp(-1.5 * x_norm**2) * np.sin(25 * np.pi * x_norm)**2)
        
        # Coupling term with non-separable interaction and chaotic modulation
        coupling = np.sum(np.sin(12 * np.pi * x_norm + 0.4 * np.sin(24 * np.pi * x_norm)) * 
                         np.cos(8 * np.pi * x_norm + 0.3 * np.cos(16 * np.pi * x_norm)) * 
                         np.exp(-0.5 * x_norm**2) * (x_norm**3 + 0.4 * x_norm**2 + 0.2 * x_norm + 0.1))
        
        # Combined objective with optimized weights for better conditioning
        return 0.22 * fractal + 0.18 * radial_grad + 0.20 * gaussian_peaks + 0.15 * trig_interf + 0.12 * barrier + 0.13 * coupling