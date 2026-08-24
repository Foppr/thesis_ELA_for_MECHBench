import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Exponential decay terms with sinusoidal modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks to increase multimodality
        cos_peaks = np.sum(np.cos(7 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Combine with different weights
        return quadratic + 0.5 * exp_decay + 0.3 * cos_peaks