import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponentially decaying sinusoidal terms with fractional frequencies
        freq_factor = 1.8 + 0.5 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.3) * np.sin(freq_factor * np.pi * x_norm**1.7) * 
                   np.cos(2.5 * freq_factor * np.pi * x_norm**1.2))
        
        # Enhanced cross-dimensional coupling with chaotic interaction terms
        f2 = np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.5 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.25 * np.abs(x_norm[:-1] - x_norm[1:])**1.6))
        
        # Multi-scale exponential decay with chaotic logarithmic modulation
        f3 = np.sum(np.exp(-0.5 * np.abs(x_norm)**1.8) * np.log(1 + 3 * np.abs(x_norm)) * 
                   np.sin(5 * x_norm) * np.cos(4 * x_norm))
        
        # Fractional power interactions with chaotic nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.1 * np.sin(3.5 * x_norm) * np.exp(-0.2 * x_norm**2.5))
        
        # Higher-order cross-dimensional terms with chaotic scaling
        f5 = np.sum((x_norm[:-1]**4 + x_norm[1:]**4) * np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(1.8 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Chaotic conditioning based on dimensionality with exponential scaling
        condition_factor = 1.1 + 0.35 * np.log(self.dim + 1) + 0.07 * np.sin(self.dim * 0.7)
        
        # Combined chaotic landscape with enhanced multi-modal structure
        result = (f1 + 0.7 * f2 + 0.5 * f3 + 0.8 * f4 + 0.4 * f5) * condition_factor
        
        # Add chaotic noise for increased complexity
        noise = 0.0015 * np.random.random() * np.sin(self.dim * 0.55)
        
        return result + noise