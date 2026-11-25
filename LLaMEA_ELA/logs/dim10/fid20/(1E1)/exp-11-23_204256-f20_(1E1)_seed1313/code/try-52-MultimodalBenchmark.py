import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with higher frequencies and chaotic modulation
        f2 = 0.5 * np.sum(np.sin(12 * np.pi * x_normalized) ** 2)
        f3 = 0.3 * np.sum(np.sin(18 * np.pi * x_normalized) ** 2)
        
        # Added cubic and higher-order polynomial terms for increased complexity
        f4 = 0.1 * np.sum(x_normalized**3)
        f5 = 0.05 * np.sum(x_normalized**5)
        
        # Additional trigonometric term with different phase and amplitude
        f6 = 0.2 * np.sum(np.cos(7 * np.pi * x_normalized) ** 2)
        
        # More complex cross-terms with exponential weighting to create sharper interactions
        f7 = 0.15 * np.sum(np.exp(0.1 * np.abs(x_normalized[:-1])) * x_normalized[:-1] ** 2 * x_normalized[1:])
        f8 = 0.12 * np.sum(np.exp(0.05 * np.abs(x_normalized[:-2])) * x_normalized[:-2] * x_normalized[1:-1] * x_normalized[2:] ** 2)
        
        # Chaotic sine-wave interaction term
        f9 = 0.08 * np.sum(np.sin(np.pi * x_normalized * (1 + 0.5 * np.sin(20 * x_normalized))) ** 2)
        
        # Exponential scaling factor based on dimensionality to increase difficulty
        adaptive_scale = 1.0 + 0.3 * np.exp(0.07 * self.dim)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)