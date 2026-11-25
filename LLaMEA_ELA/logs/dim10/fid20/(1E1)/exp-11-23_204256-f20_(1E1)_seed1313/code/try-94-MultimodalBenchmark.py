import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with slightly different frequencies and amplitudes
        f2 = 0.6 * np.sum(np.sin(15 * np.pi * x_normalized) ** 2)
        f3 = 0.25 * np.sum(np.sin(25 * np.pi * x_normalized) ** 2)
        
        # Modified polynomial terms with altered exponents
        f4 = 0.12 * np.sum(x_normalized**4)
        f5 = 0.08 * np.sum(x_normalized**6)
        
        # Additional trigonometric term with different phase and amplitude
        f6 = 0.25 * np.sum(np.cos(10 * np.pi * x_normalized) ** 2)
        
        # New cross-terms with different interaction patterns
        f7 = 0.18 * np.sum(x_normalized[:-1] ** 2 * x_normalized[1:] ** 3)
        f8 = 0.14 * np.sum(x_normalized[:-2] ** 3 * x_normalized[1:-1] * x_normalized[2:] ** 2)
        
        # Exponential scaling factor based on dimensionality to increase difficulty
        adaptive_scale = 1.0 + 0.35 * np.exp(0.08 * self.dim)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)