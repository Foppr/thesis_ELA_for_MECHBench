import numpy as np

class ChaoticCorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic component with logistic map modulation
        f1 = np.sum(1.0 / (1.0 + np.exp(-10 * (x_norm**2 - 0.5))) * 
                   (1 + 0.6 * np.sin(20 * x_norm) * np.cos(15 * x_norm)))
        
        # Nested fractal structure with recursive correlation
        f2 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                   (1 + 0.4 * np.sin(25 * x_norm) * np.cos(20 * x_norm)) * 
                   (1 + 0.3 * np.sin(18 * x_norm) * np.cos(14 * x_norm)) * 
                   (1 + 0.2 * np.sin(12 * x_norm) * np.cos(9 * x_norm)))
        
        # Adaptive amplitude with time-delayed feedback
        f3 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(16 * x_norm)) * 
                   (1 + 0.4 * np.cos(13 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.2 * np.cos(7 * x_norm)) * 
                   (1 + 0.1 * np.sin(4 * x_norm)))
        
        # Multi-scale chaotic oscillation with varying frequencies
        f4 = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                   np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                   np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Non-stationary power-law scaling with exponential decay
        f5 = np.sum(np.abs(x_norm)**1.9 * 
                   (1 + 0.3 * np.sin(14 * x_norm)) * 
                   (1 + 0.2 * np.cos(11 * x_norm)) * 
                   (1 + 0.1 * np.sin(8 * x_norm)) * 
                   (1 + 0.05 * np.cos(5 * x_norm)) * 
                   (1 + 0.02 * np.sin(3 * x_norm)))
        
        # Coupled dimension interactions with chaotic coupling strength
        f6 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.4 * np.sin(7 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(6 * x_norm[1:])) * 
                   (1 + 0.2 * np.sin(5 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(4 * x_norm[1:])) * 
                   (1 + 0.05 * np.sin(3 * x_norm[:-1])))
        
        # Memory-dependent oscillatory pattern with varying phase
        f7 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.5 * np.sin(22 * x_norm)) * 
                   (1 + 0.4 * np.cos(18 * x_norm)) * 
                   (1 + 0.3 * np.sin(15 * x_norm)) * 
                   (1 + 0.2 * np.cos(12 * x_norm)) * 
                   (1 + 0.1 * np.sin(9 * x_norm)) * 
                   (1 + 0.05 * np.cos(6 * x_norm)))
        
        # Variable scaling with chaotic exponent
        f8 = np.sum(np.abs(x_norm)**(1.7 + 0.3 * np.sin(24 * x_norm)) * 
                   (1 + 0.4 * np.sin(19 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)) * 
                   (1 + 0.2 * np.sin(13 * x_norm)) * 
                   (1 + 0.1 * np.cos(10 * x_norm)))
        
        # Multi-fractal correlation structure with exponential decay
        f9 = np.sum(np.exp(-0.6 * np.abs(x_norm)) * 
                   (1 + 0.3 * np.sin(24 * x_norm)) * 
                   (1 + 0.2 * np.cos(20 * x_norm)) * 
                   (1 + 0.1 * np.sin(16 * x_norm)) * 
                   (1 + 0.05 * np.cos(12 * x_norm)) * 
                   (1 + 0.02 * np.sin(8 * x_norm)) * 
                   (1 + 0.01 * np.cos(4 * x_norm)))
        
        # Complex basin structure with adaptive curvature
        f10 = np.sum(np.exp(-x_norm**2) * 
                    (1 + 0.5 * np.sin(21 * x_norm)) * 
                    (1 + 0.4 * np.cos(17 * x_norm)) * 
                    (1 + 0.3 * np.sin(14 * x_norm)) * 
                    (1 + 0.2 * np.cos(11 * x_norm)) * 
                    (1 + 0.1 * np.sin(8 * x_norm)) * 
                    (1 + 0.05 * np.cos(5 * x_norm)))
        
        # Final chaotic combination with global scaling
        return 3.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)