import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial growth component
        polynomial = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6)
        
        # Logarithmic barrier component
        log_barrier = -np.sum(np.log(1.0 - x_scaled**2 + 1e-10))
        
        # Sinusoidal modulation with multiple frequencies
        sinusoidal = np.sum([np.sin((i+1) * np.pi * x_scaled).sum() * 
                            np.cos((i+1) * np.pi * x_scaled).sum() 
                            for i in range(min(4, self.dim))])
        
        # Rugged terrain with exponential penalty for being near boundaries
        boundary_penalty = np.sum(np.exp(1.0 / (1.0 - np.abs(x_scaled) + 1e-10)) * (np.abs(x_scaled) > 0.9))
        
        # Combined function
        return polynomial + 0.3 * sinusoidal + 0.1 * log_barrier + 0.05 * boundary_penalty