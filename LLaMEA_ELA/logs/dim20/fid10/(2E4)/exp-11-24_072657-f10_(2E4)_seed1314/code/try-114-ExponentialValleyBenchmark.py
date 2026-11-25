import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic exponentially decaying sinusoidal terms with modified frequencies
        freq_factor = 2.5 + 0.4 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.8) * np.sin(freq_factor * np.pi * x_norm**1.5) * 
                   np.cos(2.3 * freq_factor * np.pi * x_norm**1.6))
        
        # Increased cross-dimensional coupling with stronger chaotic interaction terms
        f2 = np.sum(np.exp(-0.35 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.8 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])**1.7))
        
        # Multi-scale exponential decay with enhanced logarithmic modulation
        f3 = np.sum(np.exp(-0.45 * np.abs(x_norm)**2.2) * np.log(1 + 3.5 * np.abs(x_norm)) * 
                   np.sin(4.8 * x_norm) * np.cos(4.2 * x_norm))
        
        # Fractional power interactions with stronger nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.5 * np.sin(3.7 * x_norm) * np.exp(-0.25 * x_norm**2.9))
        
        # Higher-order cross-dimensional terms with enhanced scaling
        f5 = np.sum((x_norm[:-1]**3.8 + x_norm[1:]**3.8) * np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.2 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Enhanced chaotic conditioning based on dimensionality
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.12 * np.sin(self.dim * 0.75)
        
        # Combined chaotic landscape with improved multi-modal structure
        result = (f1 + 0.75 * f2 + 0.65 * f3 + 0.85 * f4 + 0.55 * f5) * condition_factor
        
        # Add enhanced chaotic noise for increased complexity
        noise = 0.0025 * np.random.random() * np.sin(self.dim * 0.7)
        
        return result + noise