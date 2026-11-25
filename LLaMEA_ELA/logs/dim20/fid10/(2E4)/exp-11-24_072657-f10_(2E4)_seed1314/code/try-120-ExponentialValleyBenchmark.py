import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic exponentially decaying sinusoidal terms with modified frequencies
        freq_factor = 2.3 + 0.3 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.6) * np.sin(freq_factor * np.pi * x_norm**1.7) * 
                   np.cos(2.5 * freq_factor * np.pi * x_norm**1.4))
        
        # Increased cross-dimensional coupling with stronger chaotic interaction terms
        f2 = np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.7 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.35 * np.abs(x_norm[:-1] - x_norm[1:])**1.6))
        
        # Multi-scale exponential decay with enhanced logarithmic modulation
        f3 = np.sum(np.exp(-0.5 * np.abs(x_norm)**2.0) * np.log(1 + 3.0 * np.abs(x_norm)) * 
                   np.sin(5.0 * x_norm) * np.cos(4.0 * x_norm))
        
        # Fractional power interactions with stronger nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.3 * np.sin(3.5 * x_norm) * np.exp(-0.2 * x_norm**2.7))
        
        # Higher-order cross-dimensional terms with enhanced scaling
        f5 = np.sum((x_norm[:-1]**4.0 + x_norm[1:]**4.0) * np.exp(-0.35 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.0 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Enhanced chaotic conditioning based on dimensionality
        condition_factor = 1.1 + 0.35 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.7)
        
        # Combined chaotic landscape with improved multi-modal structure
        result = (f1 + 0.8 * f2 + 0.6 * f3 + 0.9 * f4 + 0.5 * f5) * condition_factor
        
        # Add enhanced chaotic noise for increased complexity
        noise = 0.002 * np.random.random() * np.sin(self.dim * 0.65)
        
        return result + noise