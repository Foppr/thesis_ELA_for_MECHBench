import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with modified frequencies
        f2 = 0.35 * np.sum(np.sin(8 * np.pi * x_normalized) ** 2)
        f3 = 0.2 * np.sum(np.sin(12 * np.pi * x_normalized) ** 2)
        
        # Added cubic and higher-order polynomial terms for increased complexity
        f4 = 0.06 * np.sum(x_normalized**3)
        f5 = 0.025 * np.sum(x_normalized**5)
        
        # Additional trigonometric term with different phase and amplitude
        f6 = 0.12 * np.sum(np.cos(4 * np.pi * x_normalized) ** 2)
        
        # Modified cross-terms to create more complex interaction between dimensions
        f7 = 0.08 * np.sum(x_normalized[:-1] * x_normalized[1:] ** 2)
        
        # Adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7)