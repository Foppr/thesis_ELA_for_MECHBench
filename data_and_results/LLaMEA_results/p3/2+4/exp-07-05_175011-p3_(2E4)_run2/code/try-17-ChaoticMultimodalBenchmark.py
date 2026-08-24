import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic-like sinusoidal components with varying frequencies
        freqs = np.arange(1, self.dim + 1) * 1.5
        chaotic = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * np.pi * x_norm))
        
        # Nested multimodal structure with exponential scaling
        nested = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * np.pi * x_norm)**2)
        
        # Non-separable cross-term interaction with modified weighting
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * x_norm[:-1] + 3 * np.pi * x_norm[1:]))
        
        # High-frequency oscillation component with altered exponent
        high_freq = np.sum(np.sin(25 * x_norm)**3)
        
        # Additional perturbation term for increased complexity
        perturbation = np.sum(np.sin(7 * x_norm) * np.cos(4 * x_norm))
        
        # Combine all components with different weights
        return 0.7 * quadratic + 2.5 * chaotic + 1.8 * nested + 1.0 * cross_term + 1.5 * high_freq + 0.6 * perturbation