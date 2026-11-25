import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with enhanced exponential decay and fractal-like structure
        f1 = np.sum(np.exp(-0.7 * x_norm**2) * (1 + 0.8 * np.sin(15 * x_norm) * np.cos(12 * x_norm)))
        
        # Power-law correlated noise with multi-frequency sinusoidal modulation and enhanced scaling
        f2 = np.sum((1 + 0.5 * np.cos(20 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.6 * np.sin(12 * x_norm) * np.cos(9 * x_norm) * np.sin(7 * x_norm)))
        
        # Long-range dependency with fractal-like correlation structure and variable scaling
        f3 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(20 * x_norm)) * 
                   (1 + 0.4 * np.cos(15 * x_norm)) * 
                   (1 + 0.2 * np.sin(10 * x_norm)) * 
                   (1 + 0.1 * np.cos(5 * x_norm)))
        
        # Multi-scale oscillatory pattern with varying amplitudes and complex interactions
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.6 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)) * 
                   (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Basin structure with varying curvature, scaling and multi-frequency modulation
        f5 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.6 * np.sin(20 * x_norm)) * 
                   (1 + 0.5 * np.cos(17 * x_norm)) * 
                   (1 + 0.4 * np.sin(14 * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * x_norm)) * 
                   (1 + 0.2 * np.sin(8 * x_norm)))
        
        # Coupled dimension interactions with enhanced exponential weighting and multi-scale correlations
        f6 = np.sum(np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(8 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(7 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.05 * np.sin(4 * x_norm[:-1])))
        
        # Variable scaling with power-law behavior and enhanced fractal characteristics
        f7 = np.sum(np.abs(x_norm)**2.1 * 
                   (1 + 0.6 * np.sin(15 * x_norm)) * 
                   (1 + 0.5 * np.cos(13 * x_norm)) * 
                   (1 + 0.4 * np.sin(11 * x_norm)) * 
                   (1 + 0.3 * np.cos(9 * x_norm)) * 
                   (1 + 0.2 * np.sin(7 * x_norm)))
        
        # Memory effect with delayed correlation structure and enhanced multi-scale modulation
        f8 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(17 * x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)) * 
                   (1 + 0.1 * np.cos(11 * x_norm)) * 
                   (1 + 0.05 * np.sin(8 * x_norm)))
        
        # Adaptive amplitude modulation with enhanced exponential decay and multi-frequency interactions
        f9 = np.sum(np.exp(-0.3 * x_norm**2) * 
                   (1 + 0.7 * np.sin(22 * x_norm)) * 
                   (1 + 0.6 * np.cos(19 * x_norm)) * 
                   (1 + 0.5 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Combined global structure with multi-scale interactions and enhanced correlation
        f10 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                    (1 + 0.3 * np.sin(25 * x_norm)) * 
                    (1 + 0.4 * np.cos(20 * x_norm)) * 
                    (1 + 0.2 * np.sin(15 * x_norm)) * 
                    (1 + 0.1 * np.cos(10 * x_norm)) * 
                    (1 + 0.05 * np.sin(5 * x_norm)) * 
                    (1 + 0.02 * np.cos(2 * x_norm)))
        
        # Add cross-dimensional interactions with enhanced correlation structure and multi-scale modulation
        f11 = np.sum(np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                    (1 + 0.35 * np.sin(10 * x_norm[:-1])) * 
                    (1 + 0.3 * np.cos(9 * x_norm[1:])) * 
                    (1 + 0.25 * np.sin(8 * x_norm[:-1])) * 
                    (1 + 0.2 * np.cos(7 * x_norm[1:])) * 
                    (1 + 0.15 * np.sin(6 * x_norm[:-1])))
        
        # Enhanced global scaling factor with additional multi-scale components
        return 2.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)