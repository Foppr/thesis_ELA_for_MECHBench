import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with exponential decay and modified amplitude
        f1 = np.sum(np.exp(-0.5 * x_norm**2) * (1 + 0.7 * np.sin(12 * x_norm)))
        
        # Power-law correlated noise with enhanced sinusoidal modulation
        f2 = np.sum((1 + 0.4 * np.cos(18 * x_norm)) * 
                   np.exp(-0.25 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(10 * x_norm) * np.cos(7 * x_norm)))
        
        # Long-range dependency with fractal-like correlation structure and increased complexity
        f3 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                   (1 + 0.25 * np.sin(14 * x_norm)) * 
                   (1 + 0.35 * np.cos(11 * x_norm)) * 
                   (1 + 0.15 * np.sin(9 * x_norm)) * 
                   (1 + 0.1 * np.cos(8 * x_norm)))
        
        # Multi-scale oscillatory pattern with varying amplitudes and frequencies
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.6 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(11 * x_norm)) * 
                   (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Basin structure with varying curvature, scaling and additional harmonics
        f5 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.5 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)) * 
                   (1 + 0.2 * np.cos(9 * x_norm)) * 
                   (1 + 0.1 * np.sin(6 * x_norm)))
        
        # Coupled dimension interactions with enhanced exponential weighting
        f6 = np.sum(np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(3 * x_norm[1:])))
        
        # Variable scaling with power-law behavior - significant modification
        f7 = np.sum(np.abs(x_norm)**2.1 * 
                   (1 + 0.5 * np.sin(13 * x_norm)) * 
                   (1 + 0.4 * np.cos(11 * x_norm)) * 
                   (1 + 0.3 * np.sin(9 * x_norm)) * 
                   (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Memory effect with delayed correlation structure - enhanced complexity
        f8 = np.sum(np.exp(-0.45 * np.abs(x_norm)) * 
                   (1 + 0.35 * np.sin(15 * x_norm)) * 
                   (1 + 0.25 * np.cos(12 * x_norm)) * 
                   (1 + 0.15 * np.sin(10 * x_norm)) * 
                   (1 + 0.08 * np.cos(8 * x_norm)))
        
        # Adaptive amplitude modulation with exponential decay - significant change
        f9 = np.sum(np.exp(-0.25 * x_norm**2) * 
                   (1 + 0.6 * np.sin(19 * x_norm)) * 
                   (1 + 0.5 * np.cos(16 * x_norm)) * 
                   (1 + 0.4 * np.sin(13 * x_norm)) * 
                   (1 + 0.3 * np.cos(10 * x_norm)) * 
                   (1 + 0.2 * np.sin(7 * x_norm)))
        
        # Combined global structure with multi-scale interactions - altered weights
        f10 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                    (1 + 0.25 * np.sin(20 * x_norm)) * 
                    (1 + 0.35 * np.cos(17 * x_norm)) * 
                    (1 + 0.15 * np.sin(14 * x_norm)) * 
                    (1 + 0.08 * np.cos(11 * x_norm)) * 
                    (1 + 0.03 * np.sin(8 * x_norm)))
        
        # Add cross-dimensional interactions with modified correlation structure
        f11 = np.sum(np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                    (1 + 0.3 * np.sin(8 * x_norm[:-1])) * 
                    (1 + 0.25 * np.cos(7 * x_norm[1:])) * 
                    (1 + 0.2 * np.sin(6 * x_norm[:-1])) * 
                    (1 + 0.15 * np.cos(5 * x_norm[1:])))
        
        # Additional high-frequency component with complex interaction
        f12 = np.sum(np.exp(-0.1 * np.abs(x_norm)) * 
                    (1 + 0.3 * np.sin(24 * x_norm)) * 
                    (1 + 0.2 * np.cos(21 * x_norm)) * 
                    (1 + 0.15 * np.sin(18 * x_norm)) * 
                    (1 + 0.1 * np.cos(15 * x_norm)) * 
                    (1 + 0.05 * np.sin(12 * x_norm)) * 
                    (1 + 0.02 * np.cos(9 * x_norm)))
        
        # Increased overall scaling factor for more challenging optimization
        return 2.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)