import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with exponential decay and enhanced modulation
        f1 = np.sum(np.exp(-0.5 * x_norm**2) * (1 + 0.7 * np.sin(12 * x_norm)))
        
        # Power-law correlated noise with sinusoidal modulation and increased complexity
        f2 = np.sum((1 + 0.4 * np.cos(18 * x_norm)) * 
                   np.exp(-0.25 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(10 * x_norm) * np.cos(7 * x_norm)))
        
        # Long-range dependency with fractal-like correlation structure and modified scaling
        f3 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                   (1 + 0.25 * np.sin(14 * x_norm)) * 
                   (1 + 0.35 * np.cos(11 * x_norm)) * 
                   (1 + 0.15 * np.sin(9 * x_norm)))
        
        # Multi-scale oscillatory pattern with varying amplitudes and frequencies
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                   (1 + 0.6 * np.sin(16 * x_norm)) * 
                   (1 + 0.35 * np.cos(13 * x_norm)) * 
                   (1 + 0.25 * np.sin(11 * x_norm)))
        
        # Basin structure with varying curvature and scaling, enhanced with additional terms
        f5 = np.sum(np.exp(-x_norm**2) * 
                   (1 + 0.5 * np.sin(18 * x_norm)) * 
                   (1 + 0.35 * np.cos(15 * x_norm)) * 
                   (1 + 0.25 * np.sin(12 * x_norm)) * 
                   (1 + 0.15 * np.cos(9 * x_norm)))
        
        # Coupled dimension interactions with exponential weighting and increased coupling
        f6 = np.sum(np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(3 * x_norm[1:])))
        
        # Variable scaling with power-law behavior - adjusted exponents
        f7 = np.sum(np.abs(x_norm)**2.1 * 
                   (1 + 0.5 * np.sin(13 * x_norm)) * 
                   (1 + 0.4 * np.cos(11 * x_norm)) * 
                   (1 + 0.3 * np.sin(9 * x_norm)) * 
                   (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Memory effect with delayed correlation structure and increased complexity
        f8 = np.sum(np.exp(-0.45 * np.abs(x_norm)) * 
                   (1 + 0.35 * np.sin(15 * x_norm)) * 
                   (1 + 0.25 * np.cos(12 * x_norm)) * 
                   (1 + 0.15 * np.sin(10 * x_norm)) * 
                   (1 + 0.08 * np.cos(8 * x_norm)))
        
        # Adaptive amplitude modulation with exponential decay - modified parameters
        f9 = np.sum(np.exp(-0.25 * x_norm**2) * 
                   (1 + 0.6 * np.sin(19 * x_norm)) * 
                   (1 + 0.45 * np.cos(16 * x_norm)) * 
                   (1 + 0.35 * np.sin(13 * x_norm)) * 
                   (1 + 0.25 * np.cos(10 * x_norm)) * 
                   (1 + 0.15 * np.sin(7 * x_norm)))
        
        # Combined global structure with multi-scale interactions - adjusted weights and terms
        f10 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                    (1 + 0.25 * np.sin(20 * x_norm)) * 
                    (1 + 0.35 * np.cos(17 * x_norm)) * 
                    (1 + 0.15 * np.sin(14 * x_norm)) * 
                    (1 + 0.08 * np.cos(11 * x_norm)) * 
                    (1 + 0.03 * np.sin(8 * x_norm)))
        
        # Final combination with global scaling factor
        return 2.5 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)