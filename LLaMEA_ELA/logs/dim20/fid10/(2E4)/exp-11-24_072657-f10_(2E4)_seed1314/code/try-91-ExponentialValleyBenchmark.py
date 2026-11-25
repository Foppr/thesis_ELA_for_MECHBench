import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponentially decaying sinusoidal terms with fractional frequencies
        freq_factor = 2.0 + 0.6 * np.log(self.dim + 1)
        f1 = np.sum(np.exp(-np.abs(x_norm)**1.4) * np.sin(freq_factor * np.pi * x_norm**1.8) * 
                   np.cos(3.0 * freq_factor * np.pi * x_norm**1.3))
        
        # Enhanced cross-dimensional coupling with chaotic interaction terms
        f2 = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (x_norm[:-1] * x_norm[1:] + 0.6 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                   np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])**1.7))
        
        # Multi-scale exponential decay with chaotic logarithmic modulation
        f3 = np.sum(np.exp(-0.6 * np.abs(x_norm)**1.9) * np.log(1 + 4 * np.abs(x_norm)) * 
                   np.sin(6 * x_norm) * np.cos(5 * x_norm))
        
        # Fractional power interactions with chaotic nonlinearity - modified exponents
        f4 = np.sum(np.abs(x_norm)**3.0 * np.sin(4.0 * x_norm) * np.exp(-0.3 * x_norm**3.0))
        
        # Higher-order cross-dimensional terms with chaotic scaling - increased complexity
        f5 = np.sum((x_norm[:-1]**6 + x_norm[1:]**6) * np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.0 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Additional chaotic coupling with modified interaction strength
        f6 = np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(2.5 * x_norm[:-1]) * np.cos(2.5 * x_norm[1:]) * 
                   np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])**2.2))
        
        # Chaotic conditioning based on dimensionality with exponential scaling
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * 0.8)
        
        # Combined chaotic landscape with enhanced multi-modal structure
        result = (f1 + 0.8 * f2 + 0.6 * f3 + 0.9 * f4 + 0.5 * f5 + 0.7 * f6) * condition_factor
        
        # Add chaotic noise for increased complexity
        noise = 0.002 * np.random.random() * np.sin(self.dim * 0.6)
        
        return result + noise