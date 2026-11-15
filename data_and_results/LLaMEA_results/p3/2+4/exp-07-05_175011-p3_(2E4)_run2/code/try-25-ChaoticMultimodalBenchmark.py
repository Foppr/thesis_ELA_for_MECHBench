import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Enhanced chaotic-like sinusoidal components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        chaotic = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * np.pi * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Nested multimodal structure with exponential scaling and additional sinusoidal modulation
        nested = np.sum(np.exp(-np.abs(x_norm)) * (np.sin(10 * np.pi * x_norm)**2 + 0.5 * np.sin(20 * np.pi * x_norm)**2))
        
        # Stronger non-separable cross-term interaction with higher-order coupling
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * x_norm[:-1] + 2 * np.pi * x_norm[1:]) * 
                           np.cos(2 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # High-frequency oscillation component with amplitude modulation
        high_freq = np.sum(np.sin(20 * x_norm)**4 + 0.3 * np.cos(40 * x_norm)**3)
        
        # Additional chaotic modulation term with feedback-like behavior
        feedback = np.sum(np.sin(5 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)) * np.cos(15 * x_norm))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 3.0 * chaotic + 2.0 * nested + 1.2 * cross_term + 1.5 * high_freq + 0.8 * feedback