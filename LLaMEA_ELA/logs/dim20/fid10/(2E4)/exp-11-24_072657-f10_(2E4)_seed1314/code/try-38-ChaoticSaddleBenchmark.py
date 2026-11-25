import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms creating rugged terrain
        f1 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(3 * np.pi * x_norm)**2)
        
        # Complex trigonometric coupling with varying frequencies
        f2 = np.sum(np.sin(7 * x_norm) * np.cos(4 * x_norm) * np.sin(2 * x_norm))
        
        # Asymmetric gradient field with exponential weights
        f3 = np.sum(np.exp(-x_norm**2) * (x_norm**3 - 0.5 * x_norm**2 + 0.1 * x_norm))
        
        # Saddle-point interaction between pairs of dimensions
        f4 = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2)
        
        # Multi-scale chaotic oscillation terms
        f5 = np.sum(np.sin(13 * x_norm) * np.cos(11 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Asymmetric cubic polynomial with mixed signs
        f6 = np.sum(np.sign(x_norm) * np.abs(x_norm)**3 * np.cos(6 * x_norm))
        
        # Cross-dimensional interaction with exponential decay
        f7 = np.sum(np.exp(-np.abs(x_norm[:-1] + x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add small chaotic perturbation
        noise = 0.005 * np.random.random()
        
        return 0.3 * f1 + 0.7 * f2 + 0.4 * f3 + 0.6 * f4 + 0.5 * f5 + 0.8 * f6 + 0.2 * f7 + noise