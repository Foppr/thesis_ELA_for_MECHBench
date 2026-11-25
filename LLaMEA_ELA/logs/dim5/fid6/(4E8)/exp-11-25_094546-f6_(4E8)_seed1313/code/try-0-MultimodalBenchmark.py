import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial terms for smooth landscape
        poly_term = np.sum(x_norm**2)
        
        # Sine wave terms creating multiple local minima
        sine_term = np.sum(np.sin(5 * np.pi * x_norm))
        
        # Additional polynomial term to increase complexity
        extra_term = 0.1 * np.sum(x_norm**4)
        
        return poly_term + sine_term + extra_term