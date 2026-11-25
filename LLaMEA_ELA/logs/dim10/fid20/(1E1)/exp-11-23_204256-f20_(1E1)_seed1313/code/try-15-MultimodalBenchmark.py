import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with multiple frequencies
        f2 = 0.2 * np.sum(np.sin(5 * np.pi * x_normalized) ** 2)
        f3 = 0.1 * np.sum(np.sin(9 * np.pi * x_normalized) ** 2)
        
        # Quartic and higher-order polynomial terms for increased complexity
        f4 = 0.03 * np.sum(x_normalized**4)
        f5 = 0.01 * np.sum(x_normalized**6)
        
        # Additional trigonometric term with different phase and amplitude
        f6 = 0.08 * np.sum(np.cos(4 * np.pi * x_normalized) ** 2)
        
        # Cross-terms to create more complex interaction between dimensions
        f7 = 0.05 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7)