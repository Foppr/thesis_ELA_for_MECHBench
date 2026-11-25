import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponentially decaying sinusoidal terms with fractional frequencies
        freq_factor = 2.1 + 0.6 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.4) * np.sin(freq_factor * np.pi * x_norm**1.8) * 
                   np.cos(3.0 * freq_factor * np.pi * x_norm**1.3))
        
        # Enhanced cross-dimensional coupling with chaotic interaction terms
        f2 = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.6 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])**1.7))
        
        # Multi-scale exponential decay with chaotic logarithmic modulation
        f3 = np.sum(np.exp(-0.6 * np.abs(x_norm)**1.9) * np.log(1 + 4 * np.abs(x_norm)) * 
                   np.sin(6 * x_norm) * np.cos(5 * x_norm))
        
        # Fractional power interactions with chaotic nonlinearity
        f4 = np.sum(np.abs(x_norm)**2.3 * np.sin(4.0 * x_norm) * np.exp(-0.25 * x_norm**2.7))
        
        # Higher-order cross-dimensional terms with chaotic scaling
        f5 = np.sum((x_norm[:-1]**5 + x_norm[1:]**5) * np.exp(-0.35 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.0 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Chaotic conditioning based on dimensionality with exponential scaling
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.8)
        
        # Combined chaotic landscape with enhanced multi-modal structure
        result = (f1 + 0.8 * f2 + 0.6 * f3 + 0.9 * f4 + 0.5 * f5) * condition_factor
        
        # Add chaotic noise for increased complexity
        noise = 0.002 * np.random.random() * np.sin(self.dim * 0.6)
        
        # Improve fitness by adding a smooth quadratic basin term
        basin_term = 0.1 * np.sum(x_norm**2)
        
        return result + noise + basin_term