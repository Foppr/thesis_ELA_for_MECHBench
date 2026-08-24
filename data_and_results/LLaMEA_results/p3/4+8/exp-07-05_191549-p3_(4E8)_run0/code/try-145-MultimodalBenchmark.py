import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced fractal-like terrain with higher frequency sine modulation and chaotic scaling
        fractal = np.sum(np.sin(64 * np.pi * x_norm) * np.sin(32 * np.pi * x_norm) * 
                        np.sin(16 * np.pi * x_norm) * np.sin(8 * np.pi * x_norm) * 
                        np.sin(4 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Chaotic radial gradient with multiple frequency components and dynamic modulation
        r = np.linalg.norm(x_norm, axis=0)
        radial_grad = np.sum(r * np.sin(40 * np.pi * r + 0.7 * np.sin(80 * np.pi * r) + 0.3 * np.sin(120 * np.pi * r)) * 
                           np.cos(25 * np.pi * r + 0.5 * np.cos(50 * np.pi * r) + 0.2 * np.cos(75 * np.pi * r)))
        
        # Asymmetric Gaussian peaks with dynamic widths, chaotic positioning, and multi-scale modulation
        gaussian_peaks = np.sum(1.2 * np.exp(-4.0 * (x_norm - 0.25)**2 + 0.3 * np.sin(30 * np.pi * x_norm) + 0.1 * np.cos(60 * np.pi * x_norm)) + 
                               1.0 * np.exp(-3.0 * (x_norm + 0.35)**2 + 0.2 * np.cos(25 * np.pi * x_norm) + 0.15 * np.sin(50 * np.pi * x_norm)) + 
                               0.8 * np.exp(-5.0 * (x_norm - 0.55)**2 + 0.25 * np.sin(35 * np.pi * x_norm) + 0.1 * np.cos(70 * np.pi * x_norm)) + 
                               0.6 * np.exp(-2.0 * (x_norm + 0.15)**2 + 0.3 * np.cos(20 * np.pi * x_norm) + 0.2 * np.sin(40 * np.pi * x_norm)))
        
        # Enhanced trigonometric interference with higher harmonics and multi-frequency chaotic phase modulation
        trig_interf = np.sum(np.sin(40 * np.pi * x_norm + 0.5 * np.sin(80 * np.pi * x_norm) + 0.2 * np.sin(120 * np.pi * x_norm)) * 
                            np.cos(30 * np.pi * x_norm + 0.4 * np.cos(60 * np.pi * x_norm) + 0.1 * np.cos(90 * np.pi * x_norm)) * 
                            np.sin(20 * np.pi * x_norm + 0.3 * np.sin(40 * np.pi * x_norm) + 0.15 * np.sin(60 * np.pi * x_norm)) * 
                            np.cos(10 * np.pi * x_norm + 0.2 * np.cos(20 * np.pi * x_norm) + 0.1 * np.cos(30 * np.pi * x_norm)))
        
        # Advanced exponential and polynomial barrier terms with adaptive scaling and multi-scale modulation
        barrier = np.sum(np.exp(-4.0 * x_norm**2) * (x_norm**6 + 0.6 * x_norm**4 + 0.4 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm + 0.05) + 
                        0.3 * np.exp(-2.0 * x_norm**2) * np.sin(30 * np.pi * x_norm)**3 + 
                        0.15 * np.exp(-1.0 * x_norm**2) * np.cos(15 * np.pi * x_norm)**2)
        
        # Complex coupling term with non-separable interaction, chaotic modulation, and multi-scale features
        coupling = np.sum(np.sin(20 * np.pi * x_norm + 0.5 * np.sin(40 * np.pi * x_norm) + 0.2 * np.sin(60 * np.pi * x_norm)) * 
                         np.cos(15 * np.pi * x_norm + 0.4 * np.cos(30 * np.pi * x_norm) + 0.1 * np.cos(45 * np.pi * x_norm)) * 
                         np.exp(-0.7 * x_norm**2) * (x_norm**4 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.2 * x_norm + 0.1))
        
        # Combined objective with optimized weights for enhanced conditioning and algorithmic challenge
        return 0.25 * fractal + 0.20 * radial_grad + 0.22 * gaussian_peaks + 0.18 * trig_interf + 0.10 * barrier + 0.05 * coupling