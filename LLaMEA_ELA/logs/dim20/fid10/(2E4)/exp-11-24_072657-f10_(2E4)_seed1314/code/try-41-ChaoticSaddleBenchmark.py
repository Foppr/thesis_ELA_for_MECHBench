import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms creating rugged terrain with modified weights
        f1 = np.sum(0.8 * np.exp(-0.7 * np.abs(x_norm)) * np.sin(3.5 * np.pi * x_norm)**2)
        
        # Complex trigonometric coupling with varying frequencies
        f2 = np.sum(np.sin(6.5 * x_norm) * np.cos(3.5 * x_norm) * np.sin(1.8 * x_norm))
        
        # Asymmetric gradient field with exponential weights
        f3 = np.sum(0.6 * np.exp(-0.8 * x_norm**2) * (x_norm**3 - 0.4 * x_norm**2 + 0.15 * x_norm))
        
        # Saddle-point interaction between pairs of dimensions
        f4 = np.sum(0.7 * (x_norm[:-1]**2 - x_norm[1:]**2)**2)
        
        # Multi-scale chaotic oscillation terms with altered frequencies
        f5 = np.sum(0.9 * np.sin(12 * x_norm) * np.cos(10 * x_norm) * np.exp(-0.4 * x_norm**2))
        
        # Asymmetric cubic polynomial with mixed signs and modified coefficients
        f6 = np.sum(np.sign(x_norm) * 0.7 * np.abs(x_norm)**3 * np.cos(5.5 * x_norm))
        
        # Cross-dimensional interaction with exponential decay
        f7 = np.sum(0.5 * np.exp(-0.6 * np.abs(x_norm[:-1] + x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add small chaotic perturbation
        noise = 0.003 * np.random.random()
        
        return 0.4 * f1 + 0.6 * f2 + 0.5 * f3 + 0.7 * f4 + 0.4 * f5 + 0.9 * f6 + 0.3 * f7 + noise