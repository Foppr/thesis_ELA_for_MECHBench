import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical quadratic term for global structure
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-wave interactions with dynamic frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Adaptive polynomial coupling with dimension-dependent weights
        f3 = 0.5 * np.sum((x_norm**6 + 0.2 * x_norm**7 + 0.1 * x_norm**8))
        
        # Dynamic scaling based on dimensionality and interaction terms
        dynamic_scale = 1.0 + 0.2 * np.sin(self.dim * 0.5) + 0.1 * np.cos(self.dim * 0.3)
        
        # Coupled trigonometric interactions with exponential modulation
        f4 = np.sum(np.exp(-0.3 * np.sum(x_norm**2)) * np.sin(4 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # High-frequency oscillations with varying amplitudes
        f5 = 0.8 * np.sum(np.sin(15 * x_norm)**3 + np.cos(12 * x_norm)**3)
        
        # Product of dimension-wise transformed terms with varying exponents
        f6 = np.prod(np.exp(-x_norm**4) * np.sin(x_norm)**2 + 0.5 * np.cos(x_norm)**2)
        
        # Combined weighted sum with dynamic adjustment factor
        return dynamic_scale * (f1 + 0.7 * f2 + 0.3 * f3 + 0.5 * f4 + 0.6 * f5 + 0.4 * f6)