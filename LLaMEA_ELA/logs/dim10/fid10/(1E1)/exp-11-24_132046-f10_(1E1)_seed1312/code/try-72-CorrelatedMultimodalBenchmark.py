import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with sharper oscillations and exponential decay
        f1 = np.sum(np.exp(-0.3 * x_norm**2) * (1 + 0.7 * np.sin(15 * x_norm)))
        
        # Enhanced power-law correlated noise with stronger sinusoidal modulation
        f2 = np.sum((1 + 0.4 * np.cos(20 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(12 * x_norm) * np.cos(8 * x_norm)))
        
        # Strengthened long-range dependency with fractal-like correlation structure
        f3 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(14 * x_norm)) * 
                   (1 + 0.2 * np.sin(10 * x_norm)))
        
        # Enhanced multi-scale oscillatory pattern with varying amplitudes
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.6 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)))
        
        # Refined basin structure with varying curvature and scaling
        f5 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.5 * np.sin(20 * x_norm)) * 
                   (1 + 0.4 * np.cos(16 * x_norm)) * 
                   (1 + 0.3 * np.sin(13 * x_norm)) * 
                   (1 + 0.2 * np.cos(10 * x_norm)))
        
        # Enhanced coupled dimension interactions with stronger exponential weighting
        f6 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(8 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(7 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(5 * x_norm[1:])))
        
        # Improved variable scaling with power-law behavior and sharper transitions
        f7 = np.sum(np.abs(x_norm)**2.0 * 
                   (1 + 0.5 * np.sin(15 * x_norm)) * 
                   (1 + 0.4 * np.cos(12 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.2 * np.cos(8 * x_norm)))
        
        # Strengthened memory effect with delayed correlation structure
        f8 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)) * 
                   (1 + 0.2 * np.sin(13 * x_norm)) * 
                   (1 + 0.1 * np.cos(10 * x_norm)))
        
        # Enhanced adaptive amplitude modulation with exponential decay
        f9 = np.sum(np.exp(-0.3 * x_norm**2) * 
                   (1 + 0.6 * np.sin(22 * x_norm)) * 
                   (1 + 0.5 * np.cos(18 * x_norm)) * 
                   (1 + 0.4 * np.sin(15 * x_norm)) * 
                   (1 + 0.3 * np.cos(12 * x_norm)) * 
                   (1 + 0.2 * np.sin(9 * x_norm)))
        
        # Enhanced global structure with multi-scale interactions
        f10 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                    (1 + 0.3 * np.sin(25 * x_norm)) * 
                    (1 + 0.4 * np.cos(20 * x_norm)) * 
                    (1 + 0.2 * np.sin(16 * x_norm)) * 
                    (1 + 0.1 * np.cos(13 * x_norm)) * 
                    (1 + 0.05 * np.sin(10 * x_norm)))
        
        # Final combination with global scaling factor
        return 2.5 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)