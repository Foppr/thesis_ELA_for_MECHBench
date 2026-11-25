import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic quadratic with enhanced fractal curvature
        f1 = np.sum(0.4 * x_norm**2 * (1 + 0.6 * np.sin(18 * x_norm) * np.cos(15 * x_norm)))
        
        # Multi-scale chaotic gradient with improved memory effect
        f2 = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                   np.exp(-0.4 * np.abs(x_norm)) * (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)))
        
        # Directional anisotropy with enhanced fractal orientation
        f3 = np.sum(np.abs(x_norm)**1.8 * np.sin(8 * np.pi * x_norm) * 
                   (1 + 0.6 * np.cos(6 * np.pi * x_norm)) * 
                   (1 + 0.5 * np.sin(10 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.cos(12 * np.pi * x_norm)))
        
        # Dynamic basin with enhanced multi-modal transitions
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(18 * np.pi * x_norm) * 
                   (1 + 0.7 * np.cos(12 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.sin(10 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.cos(8 * np.pi * x_norm)))
        
        # Multi-scale interference with enhanced chaotic frequency modulation
        f5 = np.sum(np.sin(40 * x_norm) * np.cos(35 * x_norm) * 
                   (1 + 0.5 * np.sin(25 * x_norm)) * 
                   (1 + 0.4 * np.cos(20 * x_norm)) * 
                   (1 + 0.3 * np.sin(16 * x_norm)))
        
        # Adaptive coupling with enhanced fractal dimensional interaction
        f6 = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                   (1 + 0.6 * np.sin(6 * np.pi * x_norm[:-1])) * 
                   (1 + 0.5 * np.cos(8 * np.pi * x_norm[1:])) * 
                   (1 + 0.4 * np.sin(10 * np.pi * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(12 * np.pi * x_norm[1:])))
        
        # Enhanced fractal-like curvature with recursive scaling and memory
        f7 = np.sum(np.sin(50 * x_norm) * np.cos(45 * x_norm) * 
                   (1 + 0.4 * np.sin(30 * x_norm)) * 
                   (1 + 0.3 * np.cos(35 * x_norm)) * 
                   (1 + 0.2 * np.sin(40 * x_norm)))
        
        # Enhanced time-delayed gradient with chaotic memory effect
        f8 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(25 * np.pi * x_norm) * 
                   (1 + 0.6 * np.cos(20 * np.pi * x_norm)) * 
                   (1 + 0.5 * np.sin(15 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.cos(10 * np.pi * x_norm)))
        
        # Enhanced variable dimensional coupling with chaotic weights
        f9 = np.sum((x_norm**3.8) * (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.5 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)) * 
                   (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Enhanced fractal basin structure with chaotic transitions
        f10 = np.sum(np.exp(-0.6 * x_norm**2) * np.sin(25 * np.pi * x_norm) * 
                    (1 + 0.5 * np.cos(20 * np.pi * x_norm)) * 
                    (1 + 0.4 * np.sin(15 * np.pi * x_norm)) * 
                    (1 + 0.3 * np.cos(10 * np.pi * x_norm)) * 
                    (1 + 0.2 * np.sin(5 * np.pi * x_norm)))
        
        # Enhanced global scaling and combination with chaotic amplitude modulation
        return 3.5 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)