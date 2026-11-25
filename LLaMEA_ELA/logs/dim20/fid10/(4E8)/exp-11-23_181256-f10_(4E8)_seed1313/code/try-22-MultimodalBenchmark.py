import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Quadratic term for global basin attraction
        quadratic_term = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        sinusoidal_term = np.sum(np.sin(freqs * np.pi * x_norm) ** 2 * np.cos(freqs * 0.5 * np.pi * x_norm))
        
        # Exponential penalty term to create rugged landscape
        exp_penalty = np.sum(np.exp(-x_norm**2 / 2.0) * np.sin(3 * np.pi * x_norm)**2)
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Cross-term interaction to increase complexity
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * x_norm[:-1]))
        
        # Combine all terms with different weights
        return adaptive_scale * quadratic_term + 0.3 * sinusoidal_term - 0.1 * exp_penalty + 0.05 * cross_term