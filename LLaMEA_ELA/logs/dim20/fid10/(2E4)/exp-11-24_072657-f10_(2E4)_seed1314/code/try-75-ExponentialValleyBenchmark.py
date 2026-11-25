import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponentially decaying sinusoidal terms with adaptive frequencies
        freq_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(freq_factor * np.pi * x_norm) * 
                   np.cos(2 * freq_factor * np.pi * x_norm))
        
        # Cross-dimensional coupling with adaptive decay and interaction
        f2 = np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.3 * (x_norm[:-1]**2 - x_norm[1:]**2)) * 
                   np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale exponential decay with enhanced logarithmic modulation
        f3 = np.sum(np.exp(-0.4 * np.abs(x_norm)) * np.log(1 + 2 * np.abs(x_norm)) * 
                   np.sin(4 * x_norm) * np.cos(3 * x_norm))
        
        # Fractional power interactions with enhanced nonlinearity
        f4 = np.sum(np.abs(x_norm)**1.8 * np.sin(2.5 * x_norm) * np.exp(-0.15 * x_norm**2))
        
        # Higher-order cross-dimensional terms for increased complexity
        f5 = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning based on dimensionality with stronger scaling
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combined landscape with enhanced multi-modal structure
        result = (f1 + 0.6 * f2 + 0.4 * f3 + 0.7 * f4 + 0.3 * f5) * condition_factor
        
        # Add controlled noise for increased complexity
        noise = 0.0005 * np.random.random()
        
        return result + noise