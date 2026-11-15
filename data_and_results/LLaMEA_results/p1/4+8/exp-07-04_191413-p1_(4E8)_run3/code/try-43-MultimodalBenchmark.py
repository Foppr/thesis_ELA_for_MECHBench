import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced exponential decay terms with multiple sinusoidal modulations
        exp_decay = np.sum(np.exp(-x_scaled**2) * (np.sin(3 * np.pi * x_scaled)**2 + 
                                                   0.5 * np.sin(6 * np.pi * x_scaled)**2 + 
                                                   0.3 * np.sin(9 * np.pi * x_scaled)**2))
        
        # Additional cosine peaks with varying frequencies and amplitudes
        cos_peaks = np.sum(np.cos(7 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                          0.7 * np.cos(14 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2) + 
                          0.4 * np.cos(21 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Cross-dimensional interaction terms
        cross_interaction = np.sum(np.sin(np.pi * (x_scaled[:-1] + x_scaled[1:]))**2)
        
        # Radial symmetry terms
        radial_symmetry = np.sum(np.exp(-0.5 * (x_scaled**2).sum()) * 
                                np.cos(2 * np.pi * (x_scaled**2).sum()))
        
        # Combine with different weights
        return quadratic + 0.7 * exp_decay + 0.4 * cos_peaks + 0.2 * cross_interaction + 0.1 * radial_symmetry