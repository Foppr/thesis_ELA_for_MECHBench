import numpy as np

class CorrelatedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic with sinusoidal modulation
        f1 = np.sum(0.5 * x_norm**2 * (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Exponentially decaying correlation structure
        corr_decay = np.exp(-0.5 * np.abs(x_norm))
        f2 = np.sum(corr_decay * (1 + 0.4 * np.cos(15 * x_norm)) * 
                   (1 + 0.3 * np.sin(12 * x_norm)) * 
                   (1 + 0.2 * np.cos(8 * x_norm)))
        
        # Multi-scale sinusoidal interference
        f3 = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                   (1 + 0.5 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(14 * x_norm)) * 
                   (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Adaptive dimensionality scaling with exponential weights
        dim_weights = np.exp(-0.1 * np.arange(self.dim))
        f4 = np.sum(dim_weights * (x_norm**2.5) * (1 + 0.3 * np.cos(16 * x_norm)) * 
                   (1 + 0.2 * np.sin(13 * x_norm)))
        
        # Fractal-like periodicity with varying frequencies
        freq_mod = 1 + 0.5 * np.sin(5 * x_norm) * np.cos(7 * x_norm)
        f5 = np.sum(np.sin(freq_mod * 30 * x_norm) * 
                   (1 + 0.4 * np.cos(freq_mod * 25 * x_norm)) * 
                   (1 + 0.3 * np.sin(freq_mod * 20 * x_norm)))
        
        # Rugged landscape with multiple local minima
        f6 = np.sum(np.exp(-x_norm**2) * np.sin(22 * x_norm) * 
                   (1 + 0.6 * np.cos(18 * x_norm)) * 
                   (1 + 0.5 * np.sin(14 * x_norm)) * 
                   (1 + 0.4 * np.cos(10 * x_norm)))
        
        # Long-range interaction with power-law decay
        f7 = np.sum(np.abs(x_norm)**1.5 * np.cos(12 * x_norm) * 
                   (1 + 0.4 * np.sin(9 * x_norm)) * 
                   (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Multi-modal structure with varying amplitudes
        f8 = np.sum((x_norm**4) * (1 + 0.5 * np.sin(8 * x_norm)) * 
                   (1 + 0.4 * np.cos(6 * x_norm)) * 
                   (1 + 0.3 * np.sin(4 * x_norm)))
        
        # Boundary-sensitive region with logarithmic scaling
        boundary_effect = np.log(1 + 0.5 * np.abs(x_norm))
        f9 = np.sum(boundary_effect * (1 + 0.3 * np.cos(14 * x_norm)) * 
                   (1 + 0.2 * np.sin(11 * x_norm)))
        
        # Combined global structure with chaotic amplitude modulation
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)