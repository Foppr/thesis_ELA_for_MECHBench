import numpy as np

class ChaoticCorrelatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractional Brownian motion-like correlation structure
        f1 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm) * np.cos(8 * x_norm)) * 
                   (1 + 0.2 * np.sin(6 * x_norm) * np.cos(4 * x_norm)))
        
        # Chaotic sinusoidal modulation with varying frequencies
        f2 = np.sum(np.exp(-0.3 * x_norm**2) * 
                   (1 + 0.4 * np.sin(15 * x_norm + 0.5 * np.sin(7 * x_norm))) * 
                   (1 + 0.3 * np.cos(10 * x_norm + 0.4 * np.cos(5 * x_norm))))
        
        # Multi-scale fractal-like structure with power-law scaling
        f3 = np.sum(np.abs(x_norm)**1.7 * 
                   (1 + 0.25 * np.sin(20 * x_norm)) * 
                   (1 + 0.2 * np.cos(16 * x_norm)) * 
                   (1 + 0.15 * np.sin(12 * x_norm)) * 
                   (1 + 0.1 * np.cos(8 * x_norm)))
        
        # Long-range dependency with exponentially decaying correlations
        f4 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.35 * np.sin(14 * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * x_norm)) * 
                   (1 + 0.25 * np.sin(8 * x_norm)) * 
                   (1 + 0.2 * np.cos(5 * x_norm)) * 
                   (1 + 0.15 * np.sin(3 * x_norm)))
        
        # Non-linear transformation with chaotic behavior
        f5 = np.sum(np.exp(-0.2 * np.abs(x_norm)**1.8) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.35 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)) * 
                   (1 + 0.25 * np.cos(9 * x_norm)) * 
                   (1 + 0.2 * np.sin(6 * x_norm)) * 
                   (1 + 0.15 * np.cos(3 * x_norm)))
        
        # Cross-dimensional chaotic coupling
        f6 = np.sum(np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.3 * np.sin(9 * x_norm[:-1] + 0.2 * np.cos(4 * x_norm[1:]))) * 
                   (1 + 0.25 * np.cos(7 * x_norm[1:] + 0.15 * np.sin(3 * x_norm[:-1]))))
        
        # Multi-modal chaotic structure with varying amplitudes
        f7 = np.sum(np.exp(-0.6 * x_norm**2) * 
                   (1 + 0.5 * np.sin(25 * x_norm)) * 
                   (1 + 0.4 * np.cos(20 * x_norm)) * 
                   (1 + 0.3 * np.sin(15 * x_norm)) * 
                   (1 + 0.2 * np.cos(10 * x_norm)) * 
                   (1 + 0.1 * np.sin(5 * x_norm)))
        
        # Adaptive scaling with chaotic modulation
        f8 = np.sum(np.abs(x_norm)**2.1 * 
                   (1 + 0.3 * np.sin(16 * x_norm + 0.2 * np.sin(8 * x_norm))) * 
                   (1 + 0.25 * np.cos(12 * x_norm + 0.15 * np.cos(6 * x_norm))))
        
        # Combined chaotic landscape with variable correlation lengths
        f9 = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(17 * x_norm)) * 
                   (1 + 0.35 * np.cos(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(9 * x_norm)) * 
                   (1 + 0.25 * np.cos(5 * x_norm)) * 
                   (1 + 0.2 * np.sin(2 * x_norm)))
        
        # Final chaotic structure with non-uniform scaling
        f10 = np.sum(np.exp(-0.25 * x_norm**2) * 
                    (1 + 0.35 * np.sin(22 * x_norm)) * 
                    (1 + 0.3 * np.cos(18 * x_norm)) * 
                    (1 + 0.25 * np.sin(14 * x_norm)) * 
                    (1 + 0.2 * np.cos(10 * x_norm)) * 
                    (1 + 0.15 * np.sin(6 * x_norm)) * 
                    (1 + 0.1 * np.cos(2 * x_norm)))
        
        # Add chaotic coupling between dimensions
        f11 = np.sum(np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                    (1 + 0.3 * np.sin(8 * x_norm[:-1] + 0.2 * np.cos(4 * x_norm[1:]))) * 
                    (1 + 0.25 * np.cos(6 * x_norm[1:] + 0.15 * np.sin(3 * x_norm[:-1]))))
        
        # Return combined chaotic landscape with global scaling
        return 2.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)