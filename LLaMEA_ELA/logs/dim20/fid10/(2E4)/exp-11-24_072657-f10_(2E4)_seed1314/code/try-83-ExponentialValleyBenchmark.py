import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponentially decaying sinusoidal terms with adaptive frequencies
        freq_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(freq_factor * np.pi * x_norm) * 
                   np.cos(2 * freq_factor * np.pi * x_norm))
        
        # Cross-dimensional coupling with adaptive decay and interaction - modified weights
        f2 = np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.5 * (x_norm[:-1]**2 - x_norm[1:]**2)) * 
                   np.exp(-0.15 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale exponential decay with enhanced logarithmic modulation
        f3 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.log(1 + 3.0 * np.abs(x_norm)) * 
                   np.sin(5.0 * x_norm) * np.cos(4.0 * x_norm))
        
        # Fractional power interactions with enhanced nonlinearity - modified exponent
        f4 = np.sum(np.abs(x_norm)**2.1 * np.sin(3.0 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Higher-order cross-dimensional terms for increased complexity - modified coefficients
        f5 = np.sum((x_norm[:-1]**4 + x_norm[1:]**4) * np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Additional cubic interaction terms for enhanced ruggedness
        f6 = np.sum(x_norm[:-1]**3 * x_norm[1:]**3 * np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning based on dimensionality with stronger scaling
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined landscape with enhanced multi-modal structure - modified weights
        result = (0.85 * f1 + 0.65 * f2 + 0.45 * f3 + 0.75 * f4 + 0.35 * f5 + 0.5 * f6) * condition_factor
        
        # Add controlled noise for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise