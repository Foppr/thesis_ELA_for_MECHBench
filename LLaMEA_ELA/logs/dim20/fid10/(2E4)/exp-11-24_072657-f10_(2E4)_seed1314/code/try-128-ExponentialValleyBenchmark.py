import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic exponentially decaying sinusoidal terms with modified frequencies
        freq_factor = 3.2 + 0.4 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**2.1) * np.sin(freq_factor * np.pi * x_norm**1.6) * 
                   np.cos(2.5 * freq_factor * np.pi * x_norm**1.9))
        
        # Increased cross-dimensional coupling with stronger chaotic interaction terms
        f2 = np.sum(np.exp(-0.42 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.8 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])**2.1))
        
        # Multi-scale exponential decay with enhanced logarithmic modulation
        f3 = np.sum(np.exp(-0.45 * np.abs(x_norm)**2.3) * np.log(1 + 3.5 * np.abs(x_norm)) * 
                   np.sin(5.5 * x_norm) * np.cos(4.8 * x_norm))
        
        # Fractional power interactions with stronger nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.8 * np.sin(4.1 * x_norm) * np.exp(-0.32 * x_norm**3.1))
        
        # Higher-order cross-dimensional terms with enhanced scaling
        f5 = np.sum((x_norm[:-1]**3.9 + x_norm[1:]**3.9) * np.exp(-0.35 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.7 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Novel interaction terms with additional chaotic modulation
        f6 = np.sum(np.exp(-0.38 * np.abs(x_norm)**1.9) * np.sin(3.7 * x_norm**1.5) * 
                   np.cos(4.2 * x_norm**1.8) * (1 + 0.2 * np.sin(self.dim * 0.6 * x_norm)))
        
        # Enhanced chaotic conditioning based on dimensionality
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.2 * np.sin(self.dim * 0.9)
        
        # Combined chaotic landscape with improved multi-modal structure
        result = (f1 + 0.75 * f2 + 0.72 * f3 + 0.92 * f4 + 0.62 * f5 + 0.85 * f6) * condition_factor
        
        # Add enhanced chaotic noise for increased complexity
        noise = 0.005 * np.random.random() * np.sin(self.dim * 0.8)
        
        return result + noise