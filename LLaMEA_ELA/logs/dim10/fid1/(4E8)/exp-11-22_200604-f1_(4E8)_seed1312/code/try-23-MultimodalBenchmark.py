import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with multiple centers
        rb_fn = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(len(centers)):
            center = np.full(self.dim, centers[i])
            distance = np.sum((x_norm - center)**2)
            rb_fn += np.exp(-distance * 10) * np.cos(2 * np.pi * distance)
        
        # Polynomial decay term
        poly_term = np.sum(x_norm**6)
        
        # Sinusoidal perturbation with varying frequencies
        sin_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Combine all components
        result = rb_fn + 0.1 * poly_term + 0.05 * sin_term
        
        return result