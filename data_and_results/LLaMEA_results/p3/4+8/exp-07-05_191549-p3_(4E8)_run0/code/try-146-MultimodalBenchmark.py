import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like recursive sine-wave modulation with chaotic frequency scaling
        fractal_mod = np.sum(np.sin(20 * np.pi * x_norm + np.sin(40 * np.pi * x_norm) + 
                                   np.sin(80 * np.pi * x_norm))**2)
        
        # Adaptive radial gradient with fractal-like scaling and chaotic interference
        r = np.linalg.norm(x_norm, axis=0)
        radial_field = np.sum((r**2 + 0.01) * 
                             np.sin(15 * np.pi * r + 0.5 * np.sin(30 * np.pi * r)) * 
                             np.cos(10 * np.pi * r + 0.3 * np.sin(20 * np.pi * r)))
        
        # Multi-scale trigonometric interference with chaotic phase modulation
        trig_interf = np.sum(np.sin(25 * np.pi * x_norm + 0.4 * np.sin(50 * np.pi * x_norm)) * 
                            np.cos(20 * np.pi * x_norm + 0.3 * np.cos(40 * np.pi * x_norm)) * 
                            np.sin(15 * np.pi * x_norm + 0.2 * np.sin(30 * np.pi * x_norm)) * 
                            np.cos(12 * np.pi * x_norm + 0.1 * np.cos(24 * np.pi * x_norm)))
        
        # Mixed exponential-barrier terms with fractal-like scaling and chaotic modulation
        barrier = np.sum(np.exp(-3.0 * x_norm**2) * (x_norm**8 + 0.5 * x_norm**6 + 0.3 * x_norm**4 + 0.1 * x_norm**2 + 0.05) + 
                        0.15 * np.exp(-x_norm**2) * np.sin(25 * np.pi * x_norm)**2 + 
                        0.1 * np.exp(-1.5 * x_norm**2) * np.cos(15 * np.pi * x_norm)**3)
        
        # Coupling term with fractal-like non-separability and chaotic modulation
        coupling = np.sum(np.sin(12 * np.pi * x_norm + 0.4 * np.sin(24 * np.pi * x_norm)) * 
                         np.cos(8 * np.pi * x_norm + 0.3 * np.cos(16 * np.pi * x_norm)) * 
                         np.exp(-0.4 * x_norm**2) * (x_norm**6 + 0.4 * x_norm**4 + 0.2 * x_norm**2 + 0.05))
        
        # Asymmetric fractal Gaussian peaks with chaotic positioning and varying widths
        gaussian_peaks = np.sum(0.7 * np.exp(-3.0 * (x_norm - 0.2)**2 + 0.1 * np.sin(30 * np.pi * x_norm)) + 
                               0.5 * np.exp(-2.2 * (x_norm + 0.3)**2 + 0.15 * np.cos(25 * np.pi * x_norm)) + 
                               0.4 * np.exp(-3.5 * (x_norm - 0.5)**2 + 0.1 * np.sin(35 * np.pi * x_norm)) + 
                               0.3 * np.exp(-2.0 * (x_norm + 0.6)**2 + 0.2 * np.cos(20 * np.pi * x_norm)))
        
        # Combined objective with optimized weights for extreme conditioning
        return 0.22 * fractal_mod + 0.20 * radial_field + 0.18 * trig_interf + 0.18 * barrier + 0.14 * coupling + 0.18 * gaussian_peaks