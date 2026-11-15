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
        
        # Chaotic sine wave component with adaptive conditioning
        chaotic_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) * np.sin(3 * np.pi * x_scaled)**3)
        
        # Modified exponential decay with trigonometric modulation (new frequency)
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with different frequency and weight
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # New cross-dimensional coupling term with chaotic interaction
        cross_term = 0.15 * np.sum(np.sin(np.pi * x_scaled[:-1] * x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Add a chaotic modulation factor based on dimension
        chaos_factor = 1.0 + 0.2 * np.sin(self.dim * np.pi / 4.0)
        
        # Combine with different weights
        return chaos_factor * (quadratic + 0.5 * exp_decay + 0.3 * cos_peaks + chaotic_term + cross_term)