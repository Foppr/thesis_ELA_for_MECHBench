import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal wave components with varying frequencies
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Polynomial penalty terms to create conditioning variation
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 4) * (i + 1) * 0.01
            
        # Cross-term interactions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += x[i] * x[i + 1] * np.sin(x[i]) * 0.1
            
        # Global minimum at origin with chaotic perturbations
        base_value = np.sum(x**2) * 0.05
        chaos_factor = np.sin(np.sum(x**2)) * 0.3
        
        return base_value + wave_term + poly_term + cross_term + chaos_factor