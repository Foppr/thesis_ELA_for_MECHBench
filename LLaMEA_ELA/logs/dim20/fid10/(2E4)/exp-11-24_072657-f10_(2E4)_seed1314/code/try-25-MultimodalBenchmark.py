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
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Dynamic polynomial coupling with adaptive weights
        f3 = 0.5 * np.sum((x_norm**3 + 0.2 * x_norm**6 + 0.1 * x_norm**7))
        
        # Radial basis function with varying widths and centers
        f4 = np.sum(np.exp(-5 * (x_norm - 0.5)**2) * np.sin(4 * np.pi * x_norm))
        
        # Multi-scale trigonometric couplings creating complex landscape
        f5 = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * np.exp(-0.3 * np.sum(x_norm**2)))
        
        # High-frequency oscillations with amplitude modulation
        f6 = 0.8 * np.sum(np.sin(15 * np.pi * x_norm)**2 * np.cos(8 * np.pi * x_norm))
        
        # Adaptive scaling based on dimensionality and input magnitude
        scale_factor = 1.0 + 0.2 * (self.dim - 1) / 20.0 + 0.1 * np.mean(np.abs(x_norm))
        
        return scale_factor * (f1 + 0.7 * f2 + 0.6 * f3 + 0.5 * f4 + 0.4 * f5 + 0.9 * f6)