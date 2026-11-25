import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with enhanced adaptive curvature
        f1 = np.sum(0.3 * x_norm**2 * (1 + 0.4 * np.sin(12 * x_norm) * np.cos(8 * x_norm)))
        
        # Chaotic gradient component with improved scaling and modulation
        f2 = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                   np.exp(-0.4 * np.abs(x_norm)) * (1 + 0.3 * np.cos(10 * x_norm)) * 
                   (1 + 0.1 * np.sin(15 * x_norm)))
        
        # Enhanced directional anisotropy with stronger orientation dependency
        f3 = np.sum(np.abs(x_norm)**1.7 * np.sin(6 * np.pi * x_norm) * 
                   (1 + 0.5 * np.cos(4 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.sin(8 * np.pi * x_norm)))
        
        # Refined basin structure with improved magnitude-dependent activation
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(15 * np.pi * x_norm) * 
                   (1 + 0.6 * np.cos(10 * np.pi * x_norm)) * 
                   (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Modified multi-scale interference with better frequency separation
        f5 = np.sum(np.sin(35 * x_norm) * np.cos(30 * x_norm) * 
                   (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)))
        
        # Enhanced adaptive coupling with improved magnitude dependency
        f6 = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                   (1 + 0.5 * np.sin(5 * np.pi * x_norm[:-1])) * 
                   (1 + 0.4 * np.cos(7 * np.pi * x_norm[1:])) * 
                   (1 + 0.3 * np.sin(9 * np.pi * x_norm[:-1])))
        
        # Modified fractal-like curvature with different scaling factors
        f7 = np.sum(np.sin(45 * x_norm) * np.cos(40 * x_norm) * 
                   (1 + 0.3 * np.sin(25 * x_norm)) * 
                   (1 + 0.2 * np.cos(30 * x_norm)))
        
        # Adjusted time-delayed gradient component with stronger memory effect
        f8 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * np.sin(18 * np.pi * x_norm) * 
                   (1 + 0.5 * np.cos(14 * np.pi * x_norm)) * 
                   (1 + 0.4 * np.sin(12 * np.pi * x_norm)))
        
        # Improved variable dimensional coupling with modified weights
        f9 = np.sum((x_norm**3.5) * (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.2 * np.sin(11 * x_norm)))
        
        # Global scaling and combination with refined weights
        return 1.8 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)