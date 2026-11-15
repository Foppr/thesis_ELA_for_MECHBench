import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal modulation with chaotic behavior
        f2 = np.sum(np.sin(np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Exponential barrier terms to create complex landscape
        barriers = np.exp(-0.1 * np.sum(np.abs(x_norm)**3))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Additional high-frequency sinusoidal components for increased multimodality
        high_freq = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Cross-term interactions to increase complexity
        cross_terms = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Combine all components with different weights
        return f1 + 3.0 * f2 + 0.5 * barriers + 0.5 * chaotic + 0.8 * high_freq + 0.3 * cross_terms