import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like nested structure with chaotic scaling
        f1 = np.sum(np.abs(x_norm) ** (1.3 + 0.7 * np.sin(10 * x_norm)))
        
        # Multi-scale periodic modulation with stochastic perturbation
        f2 = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                   (1 + 0.2 * np.random.rand(self.dim)) * 
                   np.exp(-0.5 * x_norm**2))
        
        # Saddle-point interaction with asymmetric curvature
        f3 = np.sum((x_norm**2 - 1)**2 * (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Nested fractal basin with varying depth and scale
        f4 = np.sum(np.exp(-np.abs(x_norm)) * 
                   (1 + 0.4 * np.cos(20 * x_norm)) * 
                   (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(12 * x_norm)))
        
        # Chaotic oscillation with time-delayed feedback
        f5 = np.sum(np.sin(25 * x_norm) * 
                   np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.1 * np.sin(18 * x_norm)) * 
                   np.cos(14 * x_norm))
        
        # Cross-dimensional coupling with asymmetric interaction weights
        f6 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.25 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.2 * np.cos(5 * x_norm[1:])) * 
                   (1 + 0.15 * np.sin(4 * x_norm[:-1])) * 
                   (1 + 0.1 * np.cos(3 * x_norm[1:])))
        
        # Adaptive scaling with fractal dimensionality
        f7 = np.sum(np.abs(x_norm)**(1.7 + 0.3 * np.sin(14 * x_norm)) * 
                   (1 + 0.3 * np.cos(11 * x_norm)) * 
                   (1 + 0.2 * np.sin(9 * x_norm)))
        
        # Multi-scale chaotic attractor with memory effect
        f8 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                   (1 + 0.25 * np.sin(19 * x_norm)) * 
                   (1 + 0.2 * np.cos(16 * x_norm)) * 
                   (1 + 0.15 * np.sin(13 * x_norm)) * 
                   (1 + 0.1 * np.cos(10 * x_norm)))
        
        # Stochastic resonance component with controlled noise
        f9 = np.sum(np.sin(22 * x_norm) * 
                   (1 + 0.2 * np.random.rand(self.dim)) * 
                   np.exp(-0.2 * x_norm**2))
        
        # Complex basin boundary with multiple local minima
        f10 = np.sum((x_norm**4 - 2 * x_norm**2 + 1) * 
                    (1 + 0.3 * np.sin(17 * x_norm)) * 
                    (1 + 0.2 * np.cos(13 * x_norm)))
        
        # Combined chaotic landscape with variable complexity
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)