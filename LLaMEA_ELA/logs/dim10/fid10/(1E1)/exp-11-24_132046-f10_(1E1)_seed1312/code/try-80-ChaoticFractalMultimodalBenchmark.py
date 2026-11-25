import numpy as np

class ChaoticFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction component with fractional Brownian motion characteristics
        f1 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                   np.sin(25 * x_norm + np.sin(15 * x_norm)) * 
                   np.cos(20 * x_norm + np.cos(12 * x_norm)) * 
                   (1 + 0.3 * np.sin(8 * x_norm) * np.cos(6 * x_norm)))
        
        # Fractal correlation structure with recursive scaling
        f2 = np.sum(np.exp(-0.4 * np.abs(x_norm)**1.7) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.3 * np.cos(14 * x_norm)) * 
                   (1 + 0.2 * np.sin(10 * x_norm)) * 
                   (1 + 0.1 * np.cos(7 * x_norm)) * 
                   (1 + 0.05 * np.sin(4 * x_norm)))
        
        # Adaptive scaling with dynamic amplitude modulation
        f3 = np.sum(np.exp(-0.2 * np.abs(x_norm)**2.1) * 
                   (1 + 0.5 * np.sin(22 * x_norm)) * 
                   (1 + 0.4 * np.cos(19 * x_norm)) * 
                   (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(13 * x_norm)) * 
                   (1 + 0.1 * np.sin(10 * x_norm)) * 
                   (1 + 0.05 * np.cos(7 * x_norm)))
        
        # Multi-scale oscillatory pattern with chaotic frequency modulation
        f4 = np.sum(np.sin(30 * x_norm + 0.5 * np.sin(25 * x_norm)) * 
                   np.cos(28 * x_norm + 0.4 * np.cos(22 * x_norm)) * 
                   (1 + 0.3 * np.sin(18 * x_norm) * np.cos(15 * x_norm)) * 
                   (1 + 0.2 * np.sin(12 * x_norm) * np.cos(9 * x_norm)))
        
        # Basin structure with memory-dependent curvature
        f5 = np.sum(np.exp(-0.1 * x_norm**2.5) * 
                   (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(17 * x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)) * 
                   (1 + 0.1 * np.cos(11 * x_norm)) * 
                   (1 + 0.05 * np.sin(8 * x_norm)) * 
                   (1 + 0.02 * np.cos(5 * x_norm)))
        
        # Long-range dependency with exponential decay and sinusoidal modulation
        f6 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(24 * x_norm)) * 
                   (1 + 0.2 * np.cos(21 * x_norm)) * 
                   (1 + 0.1 * np.sin(18 * x_norm)) * 
                   (1 + 0.05 * np.cos(15 * x_norm)) * 
                   (1 + 0.02 * np.sin(12 * x_norm)) * 
                   (1 + 0.01 * np.cos(9 * x_norm)))
        
        # Coupled dimension interactions with chaotic coupling
        f7 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])**1.8) * 
                   (1 + 0.4 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(3 * x_norm[1:])) * 
                   (1 + 0.05 * np.sin(2 * x_norm[:-1])) * 
                   (1 + 0.02 * np.cos(x_norm[1:])))
        
        # Variable scaling with chaotic power-law behavior
        f8 = np.sum(np.abs(x_norm)**2.3 * 
                   (1 + 0.4 * np.sin(19 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)) * 
                   (1 + 0.2 * np.sin(13 * x_norm)) * 
                   (1 + 0.1 * np.cos(10 * x_norm)) * 
                   (1 + 0.05 * np.sin(7 * x_norm)) * 
                   (1 + 0.02 * np.cos(4 * x_norm)))
        
        # Memory effect with delayed chaotic correlation structure
        f9 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                   (1 + 0.35 * np.sin(23 * x_norm)) * 
                   (1 + 0.25 * np.cos(20 * x_norm)) * 
                   (1 + 0.15 * np.sin(17 * x_norm)) * 
                   (1 + 0.1 * np.cos(14 * x_norm)) * 
                   (1 + 0.05 * np.sin(11 * x_norm)) * 
                   (1 + 0.02 * np.cos(8 * x_norm)))
        
        # Adaptive amplitude modulation with chaotic decay
        f10 = np.sum(np.exp(-0.25 * x_norm**2.2) * 
                    (1 + 0.55 * np.sin(26 * x_norm)) * 
                    (1 + 0.45 * np.cos(23 * x_norm)) * 
                    (1 + 0.35 * np.sin(20 * x_norm)) * 
                    (1 + 0.25 * np.cos(17 * x_norm)) * 
                    (1 + 0.15 * np.sin(14 * x_norm)) * 
                    (1 + 0.1 * np.cos(11 * x_norm)) * 
                    (1 + 0.05 * np.sin(8 * x_norm)))
        
        # Combined global structure with chaotic multi-scale interactions
        f11 = np.sum(np.exp(-0.35 * np.abs(x_norm)**1.9) * 
                    (1 + 0.25 * np.sin(27 * x_norm)) * 
                    (1 + 0.35 * np.cos(24 * x_norm)) * 
                    (1 + 0.15 * np.sin(21 * x_norm)) * 
                    (1 + 0.1 * np.cos(18 * x_norm)) * 
                    (1 + 0.05 * np.sin(15 * x_norm)) * 
                    (1 + 0.02 * np.cos(12 * x_norm)) * 
                    (1 + 0.01 * np.sin(9 * x_norm)))
        
        # Final combination with chaotic scaling factor
        return 3.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)