import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential growth term that amplifies differences
        exp_term = np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        # Logarithmic barrier near boundaries to prevent out-of-bounds exploration
        log_barrier = np.sum(np.log(1 + 0.1 * x_scaled**2))
        
        # Periodic oscillation with varying frequencies and amplitudes
        periodic = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled**2))
        
        # Coupled sine waves creating complex interference patterns
        interference = np.sum(np.sin(np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * 
                             np.sin(4 * np.pi * x_scaled**0.5))
        
        # Combined chaotic landscape with competing forces
        return 0.3 * exp_term + 0.2 * log_barrier + 0.25 * periodic + 0.15 * interference + 0.1 * np.sum(x_scaled**4)