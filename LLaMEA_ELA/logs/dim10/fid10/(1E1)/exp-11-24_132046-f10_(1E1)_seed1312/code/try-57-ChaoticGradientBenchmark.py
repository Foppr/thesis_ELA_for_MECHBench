import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic quadratic with fractal curvature
        f1 = np.sum(0.3 * x_norm**2 * (1 + 0.5 * np.sin(15 * x_norm) * np.cos(12 * x_norm)))
        
        # Multi-scale chaotic gradient with memory effect
        f2 = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                   np.exp(-0.3 * np.abs(x_norm)) * (1 + 0.3 * np.sin(18 * x_norm)) * 
                   (1 + 0.2 * np.cos(14 * x_norm)))
        
        # Directional anisotropy with fractal orientation
        f3 = np.sum(np.abs(x_norm)**1.7 * np.sin(7 * np.pi * x_norm) * 
                   (1 + 0.5 * np.cos(5 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.sin(9 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * np.pi * x_norm)))
        
        # Dynamic basin with multi-modal transitions
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(15 * np.pi * x_norm) * 
                   (1 + 0.6 * np.cos(10 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.sin(8 * np.pi * x_norm)) * 
                   (1 + 0.2 * np.cos(6 * np.pi * x_norm)))
        
        # Multi-scale interference with chaotic frequency modulation
        f5 = np.sum(np.sin(35 * x_norm) * np.cos(30 * x_norm) * 
                   (1 + 0.4 * np.sin(22 * x_norm)) * 
                   (1 + 0.3 * np.cos(18 * x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)))
        
        # Adaptive coupling with fractal dimensional interaction
        f6 = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                   (1 + 0.5 * np.sin(5 * np.pi * x_norm[:-1])) * 
                   (1 + 0.4 * np.cos(7 * np.pi * x_norm[1:])) * 
                   (1 + 0.3 * np.sin(9 * np.pi * x_norm[:-1])) * 
                   (1 + 0.2 * np.cos(11 * np.pi * x_norm[1:])))
        
        # Fractal-like curvature with recursive scaling and memory
        f7 = np.sum(np.sin(45 * x_norm) * np.cos(40 * x_norm) * 
                   (1 + 0.3 * np.sin(25 * x_norm)) * 
                   (1 + 0.2 * np.cos(30 * x_norm)) * 
                   (1 + 0.1 * np.sin(35 * x_norm)))
        
        # Time-delayed gradient with chaotic memory effect
        f8 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * np.sin(20 * np.pi * x_norm) * 
                   (1 + 0.5 * np.cos(16 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.sin(12 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.cos(8 * np.pi * x_norm)))
        
        # Variable dimensional coupling with chaotic weights
        f9 = np.sum((x_norm**3.5) * (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.2 * np.sin(10 * x_norm)) * 
                   (1 + 0.1 * np.cos(7 * x_norm)))
        
        # Fractal basin structure with chaotic transitions
        f10 = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(22 * np.pi * x_norm) * 
                    (1 + 0.4 * np.cos(18 * np.pi * x_norm)) * 
                    (1 + 0.3 * np.sin(14 * np.pi * x_norm)) * 
                    (1 + 0.2 * np.cos(10 * np.pi * x_norm)) * 
                    (1 + 0.1 * np.sin(6 * np.pi * x_norm)))
        
        # Global scaling and combination with chaotic amplitude modulation
        return 3.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)