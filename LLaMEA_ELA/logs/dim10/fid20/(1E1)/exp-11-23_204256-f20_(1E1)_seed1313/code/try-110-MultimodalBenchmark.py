import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees
        f1 = np.sum(x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric terms with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(10 * x_norm) ** 2 + 0.3 * np.cos(15 * x_norm) ** 2)
        
        # Asymmetric logarithmic perturbations to create complex valleys
        epsilon = 1e-6
        f3 = 0.2 * np.sum(np.log(np.abs(x_norm) + epsilon) ** 2)
        
        # Cross-dimensional interactions with exponential scaling
        f4 = 0.15 * np.sum(np.exp(0.5 * x_norm[:-1] ** 2) * x_norm[1:] ** 2)
        
        # Non-central global optima by shifting the landscape
        shift = np.ones(self.dim) * 0.5
        f5 = 0.1 * np.sum((x_norm - shift)**2)
        
        # Mixed higher-order interactions
        f6 = 0.08 * np.sum(x_norm[:-2] ** 3 * x_norm[1:-1] * x_norm[2:] ** 2)
        
        # Exponential conditioning factor based on dimensionality
        cond_factor = 1.0 + 0.5 * np.exp(0.05 * self.dim)
        
        return cond_factor * (f1 + f2 + f3 + f4 + f5 + f6)