import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Global minimum at center
        center_penalty = np.sum(x**2)
        
        # Exponentially decaying sinusoidal waves
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.exp(-0.1 * (i + 1)) * np.sin(2 * np.pi * (i + 1) * x[i])
        
        # Add polynomial penalty to encourage staying near center
        poly_penalty = 0.01 * np.sum(x**4)
        
        return center_penalty + wave_term + poly_penalty