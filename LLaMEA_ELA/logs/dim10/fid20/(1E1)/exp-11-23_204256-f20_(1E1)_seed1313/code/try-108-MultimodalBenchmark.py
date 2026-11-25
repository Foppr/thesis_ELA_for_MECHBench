import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with slightly altered frequencies and amplitudes
        f2 = 0.55 * np.sum(np.sin(13 * np.pi * x_normalized) ** 2)
        f3 = 0.35 * np.sum(np.sin(21 * np.pi * x_normalized) ** 2)
        
        # Modified polynomial terms with different exponents
        f4 = 0.12 * np.sum(x_normalized**4)
        f5 = 0.07 * np.sum(x_normalized**6)
        
        # Additional trigonometric term with different phase and amplitude
        f6 = 0.22 * np.sum(np.cos(9 * np.pi * x_normalized) ** 2)
        
        # Asymmetric cross-terms to create more complex interaction between dimensions
        f7 = 0.16 * np.sum(x_normalized[:-1] ** 4 * x_normalized[1:])
        f8 = 0.13 * np.sum(x_normalized[:-2] ** 2 * x_normalized[1:-1] ** 3 * x_normalized[2:] ** 2)
        
        # Exponential scaling factor based on dimensionality to increase difficulty
        adaptive_scale = 1.0 + 0.32 * np.exp(0.075 * self.dim)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)