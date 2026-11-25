import numpy as np

class RuggedPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial landscape with varying degrees and adaptive coefficients
        f1 = np.sum((x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6) * 
                   np.exp(-0.5 * x_norm**2))
        
        # Rugged terrain with sinusoidal modulations and adaptive scaling
        f2 = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm) * 
                   np.exp(-0.3 * np.abs(x_norm)) * 
                   (1 + 0.2 * np.sin(self.dim * x_norm)))
        
        # Cross-dimensional polynomial interactions with varying weights
        f3 = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * 
                   (x_norm[:-1]**2 + x_norm[1:]**2) * 
                   np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Multi-scale ruggedness with fractional powers
        f4 = np.sum(np.abs(x_norm)**1.3 * np.sin(7 * x_norm) * 
                   np.cos(3 * x_norm) * 
                   np.exp(-0.4 * np.abs(x_norm)**1.5))
        
        # Combined landscape with enhanced multi-modality
        result = (f1 + 0.7 * f2 + 0.6 * f3 + 0.8 * f4) * condition_factor
        
        # Add controlled noise for increased complexity
        noise = 0.001 * np.random.random() * np.sin(self.dim * 0.8)
        
        return result + noise