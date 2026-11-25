import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial terms for smooth landscape
        poly_term = np.sum(x_norm**2)
        
        # Sine wave terms creating multiple local minima with varying frequencies
        sine_term = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(2 * np.abs(x_norm)))
        
        # Additional polynomial term to increase complexity and conditioning
        extra_term = 0.5 * np.sum(x_norm**6)
        
        # Cross-terms to increase interdimensional dependency and conditioning
        cross_term = 0.3 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return poly_term + sine_term + extra_term + cross_term