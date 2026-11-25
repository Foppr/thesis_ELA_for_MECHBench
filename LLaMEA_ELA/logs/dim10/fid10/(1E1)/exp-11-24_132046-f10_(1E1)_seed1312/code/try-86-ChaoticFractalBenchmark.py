import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic component with logistic map-like behavior
        f1 = np.sum(4 * x_norm * (1 - x_norm) + 0.1 * np.sin(20 * x_norm))
        
        # Fractal nested structure with recursive scaling
        f2 = np.sum(np.exp(-np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(15 * x_norm)) * 
                   (1 + 0.2 * np.cos(12 * x_norm)) * 
                   (1 + 0.1 * np.sin(9 * x_norm)))
        
        # Time-delayed sinusoidal interactions
        if self.dim > 1:
            delayed_term = np.sum(np.sin(x_norm[:-1] - 0.5 * x_norm[1:]) * 
                                np.cos(x_norm[1:] + 0.3 * x_norm[:-1]))
        else:
            delayed_term = 0.0
            
        # Non-linear power transformation with varying exponents
        f3 = np.sum(np.abs(x_norm)**(1.7 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.25 * np.cos(8 * x_norm)) * 
                   (1 + 0.15 * np.sin(6 * x_norm)))
        
        # Multi-scale oscillatory pattern with chaotic amplitude modulation
        f4 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.3 * np.cos(15 * x_norm)) * 
                   (1 + 0.2 * np.sin(12 * x_norm)))
        
        # Basin structure with varying curvature and chaotic scaling
        f5 = np.sum(np.exp(-0.5 * x_norm**2) * 
                   (1 + 0.3 * np.sin(14 * x_norm)) * 
                   (1 + 0.2 * np.cos(11 * x_norm)) * 
                   (1 + 0.1 * np.sin(8 * x_norm)) * 
                   (1 + 0.05 * np.cos(5 * x_norm)))
        
        # Coupled dimension interactions with chaotic weighting
        f6 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.2 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.15 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.1 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.05 * np.cos(3 * x_norm[1:])))
        
        # Variable scaling with chaotic power-law behavior
        f7 = np.sum(np.abs(x_norm)**(2.1 + 0.2 * np.sin(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.2 * np.cos(8 * x_norm)) * 
                   (1 + 0.1 * np.sin(6 * x_norm)))
        
        # Memory effect with chaotic correlation structure
        f8 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.25 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(13 * x_norm)) * 
                   (1 + 0.15 * np.sin(10 * x_norm)) * 
                   (1 + 0.1 * np.cos(7 * x_norm)))
        
        # Adaptive amplitude modulation with chaotic decay
        f9 = np.sum(np.exp(-0.1 * x_norm**2) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.3 * np.cos(15 * x_norm)) * 
                   (1 + 0.2 * np.sin(12 * x_norm)) * 
                   (1 + 0.1 * np.cos(9 * x_norm)) * 
                   (1 + 0.05 * np.sin(6 * x_norm)))
        
        # Combined global structure with chaotic multi-scale interactions
        f10 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                    (1 + 0.2 * np.sin(19 * x_norm)) * 
                    (1 + 0.25 * np.cos(16 * x_norm)) * 
                    (1 + 0.15 * np.sin(13 * x_norm)) * 
                    (1 + 0.1 * np.cos(10 * x_norm)) * 
                    (1 + 0.05 * np.sin(7 * x_norm)))
        
        # Final combination with chaotic scaling factor
        return 1.5 * (f1 + f2 + delayed_term + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)