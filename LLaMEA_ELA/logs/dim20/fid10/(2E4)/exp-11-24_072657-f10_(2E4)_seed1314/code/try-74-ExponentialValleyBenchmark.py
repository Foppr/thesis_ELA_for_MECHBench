import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponentially decaying sinusoidal terms with varying frequencies
        f1 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Cross-dimensional exponential coupling with decay factors
        f2 = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.5 * (x_norm[:-1]**2 - x_norm[1:]**2)))
        
        # Multi-scale exponential decay with logarithmic modulation
        f3 = np.sum(np.exp(-0.3 * np.abs(x_norm)) * np.log(1 + np.abs(x_norm)) * 
                   np.sin(5 * x_norm) * np.cos(4 * x_norm))
        
        # Fractional power interactions with varying exponents
        f4 = np.sum(np.abs(x_norm)**1.5 * np.sin(3 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combined landscape with exponential decay and multi-modal structure
        result = (f1 + 0.7 * f2 + 0.5 * f3 + 0.8 * f4) * condition_factor
        
        # Add small random perturbation for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise