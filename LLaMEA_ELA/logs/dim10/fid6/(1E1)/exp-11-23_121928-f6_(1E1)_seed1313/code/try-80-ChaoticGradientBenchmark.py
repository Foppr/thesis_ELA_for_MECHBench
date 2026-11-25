import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-wave components with exponentially decaying amplitudes
        f2 = np.sum(np.sin(20 * np.pi * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Multi-scale cosine interactions creating sharp ridges and valleys
        f3 = np.sum(np.cos(15 * np.pi * x_norm**2) * np.cos(7 * np.pi * x_norm) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Exponentially modulated Gaussian-like peaks
        f4 = np.sum(np.exp(-2 * (x_norm**2)) * np.sin(10 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Dynamic phase modulation with chaotic scaling
        phase_mod = np.sin(0.5 * np.pi * x_norm * np.exp(0.3 * x_norm**2))
        f5 = np.sum(phase_mod * np.cos(8 * np.pi * x_norm) * (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric polynomial with mixed powers
        f6 = np.sum(x_norm**3 * np.sin(6 * np.pi * x_norm) + x_norm**5 * np.cos(4 * np.pi * x_norm))
        
        # Combined hybrid fitness with adaptive weights
        return condition_factor * (0.4 * f1 + 0.25 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5 + 0.05 * f6) + 0.02 * np.sum(np.abs(x_norm)**3.5)