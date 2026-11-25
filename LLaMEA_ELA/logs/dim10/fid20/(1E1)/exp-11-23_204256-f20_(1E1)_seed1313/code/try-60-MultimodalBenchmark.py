import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees
        f1 = np.sum(x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric components with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(8 * x_norm) ** 2 + 0.5 * np.cos(12 * x_norm) ** 2)
        
        # Exponential scaling with dimensionality-dependent factor
        exp_factor = np.exp(0.05 * self.dim)
        f3 = 0.3 * exp_factor * np.sum(np.exp(2 * x_norm) - 1)
        
        # Asymmetric cross-terms creating directional bias
        f4 = 0.2 * np.sum(x_norm[:-1] ** 3 * x_norm[1:] + 0.5 * x_norm[:-1] * x_norm[1:] ** 3)
        
        # Additional sine-based interaction terms with phase shifts
        f5 = 0.25 * np.sum(np.sin(5 * x_norm + np.pi/4) * np.cos(7 * x_norm - np.pi/6))
        
        # Combined effect with adaptive scaling based on problem dimensionality
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale * (f1 + f2 + f3 + f4 + f5)