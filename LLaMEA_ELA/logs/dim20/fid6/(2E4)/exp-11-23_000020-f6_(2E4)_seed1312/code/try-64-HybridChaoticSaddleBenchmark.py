import numpy as np

class HybridChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.freqs = np.linspace(1.0, 8.0, dim)
        self.decay_rates = np.linspace(0.1, 1.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Exponential decay component with dimensionally adaptive rates
        exp_decay = np.sum(np.exp(-self.decay_rates * np.abs(x_norm)) * np.cos(self.freqs * x_norm))
        
        # Sinusoidal modulation with varying amplitudes and frequencies
        sin_mod = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                        np.sin(4 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Saddle-point geometry with hyperbolic tangent components
        saddle = np.sum(np.tanh(x_norm) * np.tanh(0.5 * x_norm) + 
                       np.tanh(2 * x_norm) * np.tanh(1.5 * x_norm))
        
        # Adaptive dimensionality scaling factor based on input magnitude
        dim_scale = 1.0 + 0.5 * np.mean(np.abs(x_norm))
        
        # Combined fitness with weighted components
        return (0.4 * exp_decay + 0.3 * sin_mod + 0.2 * saddle + 0.1 * dim_scale) * (1.0 + 0.1 * np.sum(x_norm**2))