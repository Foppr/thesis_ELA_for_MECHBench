import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base function
        quadratic = np.sum(x_norm**2)
        
        # Exponentially decaying sinusoidal terms with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        oscillatory = np.sum(np.exp(-freqs * np.abs(x_norm)) * np.sin(freqs * np.pi * x_norm))
        
        # Additional cubic penalty to encourage convergence to feasible region
        cubic_penalty = 0.01 * np.sum(np.abs(x_norm)**3)
        
        # Gradient conditioning term - increases difficulty near boundaries
        gradient_conditioning = np.sum((1.0 - np.abs(x_norm))**4)
        
        return quadratic + oscillatory + cubic_penalty + gradient_conditioning