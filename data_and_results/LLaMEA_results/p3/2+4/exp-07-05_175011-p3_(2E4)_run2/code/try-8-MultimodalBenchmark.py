import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic-like sinusoidal components with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        chaotic = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * np.pi * x_norm))
        
        # Nested multimodal structure with exponential scaling
        nested = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * np.pi * x_norm)**2)
        
        # Non-separable cross-term interaction
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * x_norm[:-1] + 2 * np.pi * x_norm[1:]))
        
        # High-frequency oscillation component
        high_freq = np.sum(np.sin(20 * x_norm)**4)
        
        # Combine all components with different weights
        return 0.5 * quadratic + 2.0 * chaotic + 1.5 * nested + 0.8 * cross_term + 1.2 * high_freq