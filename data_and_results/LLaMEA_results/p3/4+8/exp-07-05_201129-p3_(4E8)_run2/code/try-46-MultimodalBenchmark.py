import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial polynomial decay component
        radial_decay = np.sum(x_normalized**4)
        
        # Chaotic logistic map dynamics in angular space
        logistic_map = np.sum(4 * np.abs(x_normalized) * (1 - np.abs(x_normalized)))
        
        # Angular cosine modulation with varying frequencies
        angular_cos = np.sum(np.cos(10 * np.pi * np.abs(x_normalized)) * np.exp(-0.2 * np.abs(x_normalized)))
        
        # Cross-term interaction with exponential weighting
        cross_interaction = np.sum(np.exp(-0.1 * np.abs(x_normalized[:-1] * x_normalized[1:])) * (x_normalized[:-1]**2 + x_normalized[1:]**2))
        
        # High-frequency oscillation with adaptive amplitude
        high_freq_osc = np.sum(np.sin(50 * np.pi * x_normalized) * np.exp(-0.3 * np.abs(x_normalized)))
        
        # Polynomial interaction term with mixed degrees
        poly_interaction = np.sum(x_normalized**3 * np.sin(2 * np.pi * x_normalized))
        
        # Combine all components with different weights
        return 0.6 * radial_decay + 0.4 * logistic_map + 0.3 * angular_cos + 0.2 * cross_interaction + 0.15 * high_freq_osc + 0.1 * poly_interaction