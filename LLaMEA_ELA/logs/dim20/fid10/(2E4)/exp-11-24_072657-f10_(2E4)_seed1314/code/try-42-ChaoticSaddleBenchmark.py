import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with polynomial modulation
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.5) * (np.sin(3 * np.pi * x_norm)**2 + 0.1 * np.cos(5 * x_norm)))
        
        # Modified trigonometric coupling with frequency shifts
        f2 = np.sum(np.sin(7 * x_norm + 0.5 * np.sin(2 * x_norm)) * np.cos(4 * x_norm + 0.3 * np.cos(3 * x_norm)))
        
        # Improved asymmetric gradient field with multi-scale weights
        f3 = np.sum(np.exp(-x_norm**2) * (x_norm**3 - 0.3 * x_norm**2 + 0.15 * x_norm + 0.05 * np.sin(10 * x_norm)))
        
        # Enhanced saddle-point interaction with cross-dimensional coupling
        f4 = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2 + 0.1 * (x_norm[:-1] * x_norm[1:])**2)
        
        # Modified chaotic oscillation terms with variable amplitudes
        f5 = np.sum(np.sin(13 * x_norm) * np.cos(11 * x_norm) * np.exp(-0.3 * x_norm**2) * (1 + 0.2 * np.sin(7 * x_norm)))
        
        # Adjusted cubic polynomial with enhanced nonlinearity
        f6 = np.sum(np.sign(x_norm) * np.abs(x_norm)**3.5 * np.cos(6 * x_norm) * (1 + 0.1 * np.sin(4 * x_norm)))
        
        # Improved cross-dimensional interaction with adaptive weights
        f7 = np.sum(np.exp(-np.abs(x_norm[:-1] + x_norm[1:])**1.2) * (x_norm[:-1]**2 + x_norm[1:]**2 + 0.05 * x_norm[:-1] * x_norm[1:]))
        
        # Enhanced chaotic perturbation with adaptive magnitude
        noise = 0.003 * np.random.random()
        
        return 0.4 * f1 + 0.6 * f2 + 0.5 * f3 + 0.7 * f4 + 0.4 * f5 + 0.9 * f6 + 0.3 * f7 + noise