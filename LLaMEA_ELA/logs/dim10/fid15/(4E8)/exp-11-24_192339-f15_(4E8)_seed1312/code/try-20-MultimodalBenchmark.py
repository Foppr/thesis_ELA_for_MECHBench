import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with logarithmic barrier near origin
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = r * (1.0 + np.log(r + 1e-8))
        
        # Trigonometric interference pattern with varying wavelengths
        interference = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Fractal-like structure using recursive sine components
        fractal_term = np.sum(np.sin(2**np.arange(self.dim) * np.pi * x_normalized) ** 2)
        
        # Asymmetric penalty based on sign patterns
        sign_penalty = np.sum(np.abs(x_normalized) * np.exp(-np.abs(x_normalized)))
        
        # Combined landscape with non-linear weighting
        return 0.5 * radial_term + 0.4 * interference + 0.1 * fractal_term + 0.2 * sign_penalty