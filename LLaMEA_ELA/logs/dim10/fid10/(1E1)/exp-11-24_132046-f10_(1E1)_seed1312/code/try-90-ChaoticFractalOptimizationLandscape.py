import numpy as np

class ChaoticFractalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base Gaussian peak component with adaptive curvature
        f1 = np.sum(0.5 * np.exp(-0.5 * x_norm**2) * (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Nested fractal structure with chaotic scaling
        f2 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(15 * x_norm + 0.5 * np.sin(20 * x_norm))) * 
                   (1 + 0.2 * np.cos(12 * x_norm + 0.3 * np.cos(18 * x_norm))))
        
        # Time-delayed sinusoidal interactions
        delayed_x = np.roll(x_norm, 1)
        f3 = np.sum((1 + 0.3 * np.sin(8 * x_norm)) * 
                   (1 + 0.2 * np.cos(6 * x_norm)) * 
                   (1 + 0.1 * np.sin(4 * delayed_x)) * 
                   (1 + 0.05 * np.cos(3 * delayed_x)))
        
        # Multi-scale Gaussian with varying amplitudes and widths
        f4 = np.sum(np.exp(-0.2 * x_norm**2) * 
                   (1 + 0.6 * np.sin(25 * x_norm)) * 
                   (1 + 0.4 * np.cos(20 * x_norm)) * 
                   (1 + 0.2 * np.sin(15 * x_norm)) * 
                   (1 + 0.1 * np.cos(10 * x_norm)))
        
        # Chaotic modulation with exponential decay
        f5 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(18 * x_norm + 0.3 * np.sin(25 * x_norm))) * 
                   (1 + 0.3 * np.cos(14 * x_norm + 0.2 * np.cos(22 * x_norm))) * 
                   (1 + 0.1 * np.sin(10 * x_norm + 0.1 * np.sin(18 * x_norm))))
        
        # Adaptive curvature with power-law scaling
        f6 = np.sum(np.exp(-x_norm**1.8) * 
                   (1 + 0.4 * np.sin(12 * x_norm)) * 
                   (1 + 0.3 * np.cos(9 * x_norm)) * 
                   (1 + 0.2 * np.sin(6 * x_norm)) * 
                   (1 + 0.1 * np.cos(3 * x_norm)))
        
        # Multi-dimensional coupling with chaotic phase shifts
        f7 = np.sum(np.exp(-0.25 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.3 * np.sin(7 * x_norm[:-1] + 0.2 * np.cos(10 * x_norm[1:]))) * 
                   (1 + 0.2 * np.cos(5 * x_norm[1:] + 0.1 * np.sin(8 * x_norm[:-1]))))
        
        # Deceptive basin structure with nested oscillations
        f8 = np.sum(np.exp(-0.3 * x_norm**2) * 
                   (1 + 0.5 * np.sin(22 * x_norm)) * 
                   (1 + 0.4 * np.cos(19 * x_norm)) * 
                   (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(13 * x_norm)) * 
                   (1 + 0.1 * np.sin(10 * x_norm)))
        
        # Fractal-like correlation with delayed feedback
        f9 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(16 * x_norm + 0.2 * np.sin(24 * x_norm))) * 
                   (1 + 0.3 * np.cos(13 * x_norm + 0.1 * np.cos(21 * x_norm))) * 
                   (1 + 0.2 * np.sin(10 * x_norm + 0.05 * np.sin(18 * x_norm))))
        
        # Combined chaotic landscape with variable scaling
        f10 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                    (1 + 0.6 * np.sin(20 * x_norm)) * 
                    (1 + 0.5 * np.cos(17 * x_norm)) * 
                    (1 + 0.4 * np.sin(14 * x_norm)) * 
                    (1 + 0.3 * np.cos(11 * x_norm)) * 
                    (1 + 0.2 * np.sin(8 * x_norm)) * 
                    (1 + 0.1 * np.cos(5 * x_norm)))
        
        # Final combined chaotic structure
        return 1.5 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)