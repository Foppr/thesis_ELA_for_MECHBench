import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = np.linspace(1.0, 10.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay components
        exp_terms = np.exp(-self.conditioning * np.abs(x_scaled))
        
        # Sinusoidal modulation with varying frequencies
        sin_modulation = np.sum(np.sin(self.conditioning * x_scaled) * 
                               np.cos(2 * self.conditioning * x_scaled))
        
        # Adaptive conditioning effect
        adaptive_term = np.sum(self.conditioning * (x_scaled ** 2) * np.exp(-x_scaled ** 2))
        
        # Combine all terms with different weights
        result = np.sum(exp_terms) + 0.5 * sin_modulation**2 + 0.1 * adaptive_term
        
        # Add small random noise for ruggedness
        noise = 0.001 * np.random.rand()
        
        return result + noise