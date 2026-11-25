import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with enhanced exponential decay and modified sinusoidal modulation
        f1 = np.sum(np.exp(-0.7 * x_norm**2) * (1 + 0.8 * np.sin(12 * x_norm)))
        
        # Power-law correlated noise with amplified sinusoidal modulation and adjusted scaling
        f2 = np.sum((1 + 0.5 * np.cos(20 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.6 * np.sin(10 * x_norm) * np.cos(8 * x_norm)))
        
        # Long-range dependency with enhanced fractal-like correlation structure and increased complexity
        f3 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(15 * x_norm)) * 
                   (1 + 0.5 * np.cos(12 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Multi-scale oscillatory pattern with enhanced amplitude variations and additional frequency components
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.7 * np.sin(18 * x_norm)) * 
                   (1 + 0.5 * np.cos(15 * x_norm)) * 
                   (1 + 0.4 * np.sin(13 * x_norm)) * 
                   (1 + 0.2 * np.cos(11 * x_norm)))
        
        # Basin structure with enhanced curvature, scaling, and additional modulation
        f5 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.6 * np.sin(20 * x_norm)) * 
                   (1 + 0.5 * np.cos(17 * x_norm)) * 
                   (1 + 0.4 * np.sin(14 * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * x_norm)) * 
                   (1 + 0.2 * np.sin(8 * x_norm)))
        
        # Coupled dimension interactions with enhanced exponential weighting and increased correlation
        f6 = np.sum(np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(7 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(6 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(5 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(4 * x_norm[1:])))
        
        # Variable scaling with enhanced power-law behavior and additional modulation
        f7 = np.sum(np.abs(x_norm)**2.2 * 
                   (1 + 0.6 * np.sin(14 * x_norm)) * 
                   (1 + 0.5 * np.cos(12 * x_norm)) * 
                   (1 + 0.4 * np.sin(10 * x_norm)) * 
                   (1 + 0.3 * np.cos(8 * x_norm)))
        
        # Memory effect with delayed correlation structure and increased complexity
        f8 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(11 * x_norm)) * 
                   (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Adaptive amplitude modulation with enhanced exponential decay and additional frequency components
        f9 = np.sum(np.exp(-0.3 * x_norm**2) * 
                   (1 + 0.7 * np.sin(20 * x_norm)) * 
                   (1 + 0.6 * np.cos(17 * x_norm)) * 
                   (1 + 0.5 * np.sin(14 * x_norm)) * 
                   (1 + 0.4 * np.cos(11 * x_norm)) * 
                   (1 + 0.3 * np.sin(8 * x_norm)) * 
                   (1 + 0.2 * np.cos(5 * x_norm)))
        
        # Combined global structure with multi-scale interactions and enhanced weights
        f10 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                    (1 + 0.3 * np.sin(20 * x_norm)) * 
                    (1 + 0.4 * np.cos(17 * x_norm)) * 
                    (1 + 0.2 * np.sin(14 * x_norm)) * 
                    (1 + 0.1 * np.cos(11 * x_norm)) * 
                    (1 + 0.05 * np.sin(8 * x_norm)) * 
                    (1 + 0.03 * np.cos(5 * x_norm)))
        
        # Add cross-dimensional interactions with enhanced correlation structure and additional components
        f11 = np.sum(np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                    (1 + 0.3 * np.sin(9 * x_norm[:-1])) * 
                    (1 + 0.25 * np.cos(8 * x_norm[1:])) * 
                    (1 + 0.2 * np.sin(7 * x_norm[:-1])) * 
                    (1 + 0.15 * np.cos(6 * x_norm[1:])))
        
        # Enhanced global scaling factor with additional modulation
        return 2.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)