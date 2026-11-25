import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive curvature
        f1 = np.sum(0.5 * x_norm**2 * (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Chaotic gradient component with dynamic scaling
        f2 = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                   np.exp(-0.5 * np.abs(x_norm)) * (1 + 0.2 * np.cos(8 * x_norm)))
        
        # Directional anisotropy with adaptive orientation
        f3 = np.sum(np.abs(x_norm)**1.5 * np.sin(5 * np.pi * x_norm) * 
                   (1 + 0.4 * np.cos(3 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Dynamic basin structure with magnitude-dependent activation
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(12 * np.pi * x_norm) * 
                   (1 + 0.5 * np.cos(9 * np.pi * x_norm)) * 
                   (1 + 0.2 * np.sin(6 * np.pi * x_norm)))
        
        # Multi-scale interference with adaptive frequency modulation
        f5 = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                   (1 + 0.3 * np.sin(18 * x_norm)) * 
                   (1 + 0.2 * np.cos(14 * x_norm)))
        
        # Adaptive coupling with input magnitude dependency
        f6 = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                   (1 + 0.4 * np.sin(4 * np.pi * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(6 * np.pi * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(8 * np.pi * x_norm[:-1])))
        
        # Fractal-like curvature with recursive scaling
        f7 = np.sum(np.sin(40 * x_norm) * np.cos(35 * x_norm) * 
                   (1 + 0.2 * np.sin(22 * x_norm)) * 
                   (1 + 0.1 * np.cos(28 * x_norm)))
        
        # Time-delayed gradient component with memory effect
        f8 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * np.sin(16 * np.pi * x_norm) * 
                   (1 + 0.4 * np.cos(12 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * np.pi * x_norm)))
        
        # Variable dimensional coupling with dynamic weights
        f9 = np.sum((x_norm**3) * (1 + 0.2 * np.sin(14 * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * x_norm)) * 
                   (1 + 0.1 * np.sin(9 * x_norm)))
        
        # Global scaling and combination
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)