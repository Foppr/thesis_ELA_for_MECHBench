import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave with exponentially decaying amplitude
        f2 = np.sum(np.sin(2 * np.pi * x_norm * np.exp(-0.1 * np.abs(x_norm))) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Multi-scale cosine product with dynamic frequency modulation
        frequencies = 1 + 0.5 * np.sin(np.linspace(0, np.pi, self.dim) * x_norm)
        f3 = np.prod(np.cos(frequencies * x_norm**2))
        
        # Adaptive basin depth term based on dimensionality
        basin_depth = 1.0 / (1.0 + np.exp(-self.dim * 0.3 * x_norm))
        f4 = np.sum(basin_depth * np.sin(5 * x_norm)**2)
        
        # Exponentially weighted harmonic interaction
        weights = np.exp(-0.2 * np.arange(self.dim))
        f5 = np.sum(weights * np.sin(7 * x_norm) * np.cos(3 * x_norm**2))
        
        # Dynamic phase shift modulated by dimensionality
        phase_shift = np.sum(np.sin(0.5 * np.pi * x_norm * (1 + 0.1 * self.dim)) * np.cos(0.2 * np.pi * x_norm**3))
        
        # Combined with a polynomial correction term
        f6 = np.sum(x_norm**4 * np.cos(2.5 * x_norm))
        
        # Final hybrid function with dynamic scaling
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        return scale * (0.4 * f1 + 0.25 * f2 + 0.15 * f3 - 0.1 * f4 + 0.08 * f5 + 0.05 * phase_shift + 0.02 * f6) + 0.01 * np.sum(np.abs(x_norm)**3)