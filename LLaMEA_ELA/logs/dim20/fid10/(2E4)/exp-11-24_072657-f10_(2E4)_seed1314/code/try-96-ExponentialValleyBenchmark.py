import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponentially decaying sinusoidal terms with fractional frequencies
        freq_factor = 2.1 + 0.4 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.4) * np.sin(freq_factor * np.pi * x_norm**1.6) * 
                   np.cos(2.3 * freq_factor * np.pi * x_norm**1.3))
        
        # Enhanced cross-dimensional coupling with chaotic interaction terms
        f2 = np.sum(np.exp(-0.35 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.6 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])**1.5))
        
        # Multi-scale exponential decay with chaotic logarithmic modulation
        f3 = np.sum(np.exp(-0.45 * np.abs(x_norm)**1.9) * np.log(1 + 2.5 * np.abs(x_norm)) * 
                   np.sin(4.8 * x_norm) * np.cos(3.7 * x_norm))
        
        # Fractional power interactions with chaotic nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.2 * np.sin(3.2 * x_norm) * np.exp(-0.18 * x_norm**2.6))
        
        # Higher-order cross-dimensional terms with chaotic scaling
        f5 = np.sum((x_norm[:-1]**3.8 + x_norm[1:]**3.8) * np.exp(-0.32 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(1.9 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Chaotic conditioning based on dimensionality with exponential scaling
        condition_factor = 1.05 + 0.4 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * 0.65)
        
        # Combined chaotic landscape with enhanced multi-modal structure
        result = (f1 + 0.75 * f2 + 0.55 * f3 + 0.85 * f4 + 0.45 * f5) * condition_factor
        
        # Add chaotic noise for increased complexity
        noise = 0.0018 * np.random.random() * np.sin(self.dim * 0.6)
        
        return result + noise