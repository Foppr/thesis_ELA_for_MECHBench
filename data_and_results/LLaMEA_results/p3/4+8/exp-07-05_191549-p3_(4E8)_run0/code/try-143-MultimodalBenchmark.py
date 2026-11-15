import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like recursive sine-wave modulation with varying frequencies and amplitudes
        fractal_mod = np.sum(np.sin(25 * np.pi * x_norm + 0.3 * np.sin(50 * np.pi * x_norm)) * 
                            np.cos(19 * np.pi * x_norm + 0.2 * np.cos(38 * np.pi * x_norm)) * 
                            np.sin(13 * np.pi * x_norm + 0.4 * np.sin(26 * np.pi * x_norm)) * 
                            np.cos(9 * np.pi * x_norm + 0.1 * np.cos(18 * np.pi * x_norm)))
        
        # Adaptive radial gradient field with chaotic scaling and multi-scale interference
        r = np.linalg.norm(x_norm, axis=0)
        radial_grad = np.sum((r + 0.03) * 
                           np.sin(20 * np.pi * r + 3 * np.sin(40 * np.pi * r)) * 
                           np.cos(15 * np.pi * r + 2 * np.cos(30 * np.pi * r)) * 
                           np.sin(10 * np.pi * r + 1.5 * np.sin(20 * np.pi * r)))
        
        # Asymmetric Gaussian peaks with fractal positioning and varying widths
        gaussian_peaks = np.sum(0.75 * np.exp(-3.2 * (x_norm - 0.31)**2 + 0.15 * np.sin(25 * np.pi * x_norm)) + 
                               0.52 * np.exp(-2.5 * (x_norm + 0.41)**2 + 0.18 * np.cos(20 * np.pi * x_norm)) + 
                               0.42 * np.exp(-3.8 * (x_norm - 0.61)**2 + 0.12 * np.sin(30 * np.pi * x_norm)) + 
                               0.35 * np.exp(-2.9 * (x_norm + 0.21)**2 + 0.14 * np.cos(15 * np.pi * x_norm)))
        
        # Mixed exponential and polynomial barrier with chaotic modulation and multi-scale scaling
        barrier = np.sum(np.exp(-3.2 * x_norm**2) * (x_norm**7 + 0.5 * x_norm**5 + 0.25 * x_norm**3 + 0.08) + 
                        0.15 * np.exp(-x_norm**2) * np.sin(25 * np.pi * x_norm)**2 + 
                        0.08 * np.exp(-1.5 * x_norm**2) * np.cos(15 * np.pi * x_norm)**3)
        
        # Coupling term with non-separable interaction, fractal modulation, and multi-scale interference
        coupling = np.sum(np.sin(11 * np.pi * x_norm + 0.4 * np.sin(22 * np.pi * x_norm)) * 
                         np.cos(8 * np.pi * x_norm + 0.3 * np.cos(16 * np.pi * x_norm)) * 
                         np.exp(-0.4 * x_norm**2) * (x_norm**5 + 0.35 * x_norm**3 + 0.08))
        
        # Trigonometric interference with recursive chaotic phase modulation and multi-frequency mixing
        trig_interf = np.sum(np.sin(22 * np.pi * x_norm + 0.6 * np.sin(44 * np.pi * x_norm)) * 
                            np.cos(18 * np.pi * x_norm + 0.5 * np.cos(36 * np.pi * x_norm)) * 
                            np.sin(14 * np.pi * x_norm + 00.4 * np.sin(28 * np.pi * x_norm)) * 
                            np.cos(11 * np.pi * x_norm + 0.3 * np.cos(22 * np.pi * x_norm)) * 
                            np.sin(7 * np.pi * x_norm + 0.2 * np.sin(14 * np.pi * x_norm)))
        
        # Combined objective with optimized weights for extreme conditioning and challenge
        return 0.25 * fractal_mod + 0.20 * radial_grad + 0.18 * gaussian_peaks + 0.17 * barrier + 0.14 * coupling + 0.06 * trig_interf