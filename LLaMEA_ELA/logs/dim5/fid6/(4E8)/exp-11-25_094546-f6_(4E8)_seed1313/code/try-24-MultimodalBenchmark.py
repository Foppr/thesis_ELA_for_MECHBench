import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial terms with adaptive weights
        poly_weights = np.arange(1, self.dim + 1)
        poly_term = np.sum(poly_weights * (x_norm**2))
        
        # High-frequency sine waves creating complex landscape
        sine_term = np.sum(np.sin(10 * np.pi * x_norm))
        
        # Additional cosine terms for increased complexity
        cos_term = np.sum(np.cos(7 * np.pi * x_norm))
        
        # Fourth-order polynomial for additional curvature
        quartic_term = 0.1 * np.sum(x_norm**4)
        
        # Mixed polynomial and trigonometric terms for challenging interactions
        mixed_term = 0.05 * np.sum((x_norm**3) * np.sin(3 * np.pi * x_norm))
        
        return poly_term + sine_term + cos_term + quartic_term + mixed_term