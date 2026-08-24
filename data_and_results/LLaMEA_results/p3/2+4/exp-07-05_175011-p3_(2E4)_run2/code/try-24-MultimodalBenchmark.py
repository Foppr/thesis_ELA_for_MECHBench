import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic-like sinusoidal components with varying frequencies and amplitude modulation
        freqs = np.arange(1, self.dim + 1)
        chaotic = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * np.pi * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Nested multimodal structure with exponential scaling and polynomial modulation
        nested = np.sum(np.exp(-np.abs(x_norm)) * (np.sin(10 * np.pi * x_norm)**2 + 0.5 * np.sin(20 * np.pi * x_norm)**2))
        
        # Non-separable cross-term interaction with higher-order polynomial coupling
        cross_term = np.sum(x_norm[:-1]**3 * x_norm[1:]**2 * np.sin(3 * np.pi * x_norm[:-1] + 2 * np.pi * x_norm[1:]))
        
        # High-frequency oscillation component with varying amplitudes
        high_freq = np.sum(np.sin(20 * x_norm)**4 + 0.3 * np.cos(30 * x_norm)**3)
        
        # Additional complex interaction term with trigonometric polynomial
        complex_interaction = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 2.5 * chaotic + 1.8 * nested + 1.0 * cross_term + 1.5 * high_freq + 0.7 * complex_interaction