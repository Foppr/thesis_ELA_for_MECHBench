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
        chaotic_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Modified exponential decay with trigonometric modulation (higher frequency)
        exp_decay = np.sum(np.exp(-2 * x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with varying frequency and weight
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Enhanced cross-dimensional interaction term with non-linear coupling
        cross_term = 0.15 * np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Add a small chaotic perturbation for increased complexity
        chaotic_perturbation = 0.05 * np.sum(np.sin(100 * x_scaled) * np.cos(50 * x_scaled))
        
        # Combine with different weights
        return quadratic + 0.7 * exp_decay + 0.25 * cos_peaks + 0.1 * chaotic_term + 0.1 * cross_term + chaotic_perturbation