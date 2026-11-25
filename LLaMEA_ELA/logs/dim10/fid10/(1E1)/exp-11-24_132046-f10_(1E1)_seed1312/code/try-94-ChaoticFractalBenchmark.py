import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like nested structure with recursive scaling
        f1 = np.sum(np.sinh(3 * x_norm) * np.exp(-0.5 * x_norm**2) * 
                   (1 + 0.3 * np.sin(7 * x_norm)) * 
                   (1 + 0.2 * np.cos(5 * x_norm)))
        
        # Time-delayed feedback with asymmetric hyperbolic sine
        f2 = np.sum(np.sinh(2 * x_norm[:-1]) * np.cosh(1.5 * x_norm[1:]) * 
                   (1 + 0.4 * np.sin(9 * x_norm[:-1])) * 
                   (1 + 0.3 * np.cos(6 * x_norm[1:])) * 
                   np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Nested fractal basin with varying curvature and scaling
        f3 = np.sum(np.tanh(2.5 * x_norm) * (1 + 0.2 * np.sin(8 * x_norm)) * 
                   (1 + 0.1 * np.cos(4 * x_norm)) * 
                   np.exp(-0.4 * np.abs(x_norm)**1.7))
        
        # Asymmetric multi-scale oscillatory pattern
        f4 = np.sum(np.sinh(4 * x_norm) * np.cosh(3 * x_norm) * 
                   (1 + 0.5 * np.sin(12 * x_norm)) * 
                   (1 + 0.3 * np.cos(9 * x_norm)) * 
                   (1 + 0.2 * np.sin(6 * x_norm)))
        
        # Chaotic interaction with exponential decay and delayed correlation
        f5 = np.sum(np.exp(-x_norm**2) * np.tanh(2 * x_norm) * 
                   (1 + 0.3 * np.sin(10 * x_norm)) * 
                   (1 + 0.2 * np.cos(7 * x_norm)) * 
                   (1 + 0.1 * np.sin(4 * x_norm)))
        
        # Multi-dimensional asymmetric scaling with fractal-like behavior
        f6 = np.sum(np.abs(x_norm)**2.3 * np.sinh(1.5 * x_norm) * 
                   (1 + 0.4 * np.cos(8 * x_norm)) * 
                   (1 + 0.3 * np.sin(5 * x_norm)) * 
                   (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Delayed feedback with hyperbolic sine and cosine coupling
        f7 = np.sum(np.sinh(1.8 * x_norm[:-1]) * np.cosh(2.2 * x_norm[1:]) * 
                   (1 + 0.25 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.2 * np.cos(4 * x_norm[1:])) * 
                   np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Nested basin structure with varying curvature and chaotic modulation
        f8 = np.sum(np.tanh(3 * x_norm) * (1 + 0.3 * np.cos(6 * x_norm)) * 
                   (1 + 0.2 * np.sin(4 * x_norm)) * 
                   np.exp(-0.5 * np.abs(x_norm)**2.1))
        
        # Asymmetric multi-scale interaction with exponential weighting
        f9 = np.sum(np.sinh(2.5 * x_norm) * (1 + 0.4 * np.cos(7 * x_norm)) * 
                   (1 + 0.3 * np.sin(5 * x_norm)) * 
                   (1 + 0.2 * np.cos(3 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)**1.8))
        
        # Global chaotic structure with time-delayed feedback
        f10 = np.sum(np.tanh(2 * x_norm) * np.sinh(1.5 * x_norm) * 
                    (1 + 0.35 * np.sin(9 * x_norm)) * 
                    (1 + 0.25 * np.cos(6 * x_norm)) * 
                    (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Final combination with global scaling factor
        return 1.5 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)