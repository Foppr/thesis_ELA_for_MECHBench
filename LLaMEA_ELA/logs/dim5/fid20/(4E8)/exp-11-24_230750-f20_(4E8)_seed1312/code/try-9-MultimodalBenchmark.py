import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(10 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Radial basin term with exponential decay
        radius = np.sqrt(np.sum(x_norm**2))
        f3 = 0.3 * np.exp(-radius) * np.sin(8 * np.pi * radius)
        
        # Cross-terms creating complex interaction between dimensions
        f4 = 0.1 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(7 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # High-frequency oscillation in all dimensions
        f5 = 0.2 * np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm))
        
        # Add a quartic term to increase complexity
        f6 = 0.05 * np.sum(x_norm**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6