import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift input to center the global minimum at (1,1,...,1)
        x_shifted = x - 1.0
        
        # Scale input to [-1, 1] range
        x_scaled = x_shifted / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Exponential decay terms with sinusoidal modulation (modified frequency)
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with different frequency and weight
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Add a cross-dimensional interaction term with higher coupling strength
        cross_term = 0.2 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Add a chaotic sine-wave component for increased multimodality
        chaotic_term = 0.1 * np.sum(np.sin(13 * np.pi * x_scaled) * np.cos(17 * np.pi * x_scaled))
        
        # Combine with different weights
        return quadratic + 0.7 * exp_decay + 0.3 * cos_peaks + cross_term + chaotic_term