import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic base with sinusoidal modulation and exponential decay
        f1 = np.sum(np.exp(-0.5 * x_norm**2) * (1 + 0.3 * np.sin(12 * x_norm) * np.cos(8 * x_norm)))
        
        # Saddle point structure with hyperbolic tangent interactions
        f2 = np.sum(np.tanh(x_norm) * np.sin(10 * x_norm) * (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Power-law scaling with fractal-like correlation
        f3 = np.sum(np.abs(x_norm)**1.7 * (1 + 0.4 * np.sin(9 * x_norm)) * (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Multi-scale oscillatory pattern with chaotic amplitude modulation
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                   (1 + 0.3 * np.sin(15 * x_norm)) * 
                   (1 + 0.2 * np.cos(10 * x_norm)) * 
                   (1 + 0.1 * np.sin(5 * x_norm)))
        
        # Cross-dimensional coupling with chaotic correlation structure
        f5 = np.sum(np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.25 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.2 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.15 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(3 * x_norm[1:])))
        
        # Basin structure with varying curvature and chaotic scaling
        f6 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.3 * np.sin(15 * x_norm)) * 
                   (1 + 0.2 * np.cos(12 * x_norm)) * 
                   (1 + 0.1 * np.sin(9 * x_norm)) * 
                   (1 + 0.05 * np.cos(6 * x_norm)))
        
        # Memory effect with delayed chaotic correlation
        f7 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)) * 
                   (1 + 0.15 * np.cos(11 * x_norm)) * 
                   (1 + 0.1 * np.sin(8 * x_norm)) * 
                   (1 + 0.05 * np.cos(5 * x_norm)))
        
        # Adaptive chaotic modulation with exponential decay
        f8 = np.sum(np.exp(-0.25 * x_norm**2) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.3 * np.cos(15 * x_norm)) * 
                   (1 + 0.2 * np.sin(12 * x_norm)) * 
                   (1 + 0.1 * np.cos(9 * x_norm)) * 
                   (1 + 0.05 * np.sin(6 * x_norm)))
        
        # Combined chaotic structure with multi-scale interactions
        f9 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                   (1 + 0.25 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(13 * x_norm)) * 
                   (1 + 0.15 * np.sin(10 * x_norm)) * 
                   (1 + 0.1 * np.cos(7 * x_norm)) * 
                   (1 + 0.05 * np.sin(4 * x_norm)))
        
        # Add chaotic dimension interactions
        f10 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                    (1 + 0.3 * np.sin(8 * x_norm[:-1])) * 
                    (1 + 0.25 * np.cos(7 * x_norm[1:])) * 
                    (1 + 0.2 * np.sin(6 * x_norm[:-1])) * 
                    (1 + 0.15 * np.cos(5 * x_norm[1:])))
        
        # Final chaotic scaling factor
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)