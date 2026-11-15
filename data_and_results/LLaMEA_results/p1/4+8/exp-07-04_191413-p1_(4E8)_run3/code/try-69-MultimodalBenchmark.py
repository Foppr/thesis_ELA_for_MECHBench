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
        
        # Enhanced exponential decay with chaotic sine wave modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with chaotic frequency and weight
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Chaotic sine wave component with adaptive conditioning
        chaotic_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2) * np.sin(13 * x_scaled))
        
        # Enhanced cross-dimensional interaction term with non-linear coupling
        cross_term = 0.15 * np.sum(x_scaled[:-1]**2 * x_scaled[1:]**2)
        
        # Add a new frequency term with different weighting
        freq_term = 0.05 * np.sum(np.sin(17 * np.pi * x_scaled) * np.cos(19 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return quadratic + 0.7 * exp_decay + 0.25 * cos_peaks + 0.1 * chaotic_term + 0.05 * freq_term + cross_term