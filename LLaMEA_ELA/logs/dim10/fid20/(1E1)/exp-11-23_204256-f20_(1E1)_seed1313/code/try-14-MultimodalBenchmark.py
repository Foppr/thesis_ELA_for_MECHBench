import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic sine-wave perturbations with varying amplitudes and frequencies
        f2 = 0.3 * np.sum(np.sin(7 * np.pi * x_normalized) ** 3)
        f3 = 0.25 * np.sum(np.sin(11 * np.pi * x_normalized) ** 4)
        
        # Exponential and higher-order polynomial terms for increased complexity
        f4 = 0.05 * np.sum(np.exp(2 * x_normalized**2) - 1)
        f5 = 0.02 * np.sum(x_normalized**8)
        
        # Additional trigonometric term with non-linear phase modulation
        f6 = 0.1 * np.sum(np.cos(6 * np.pi * x_normalized + np.sin(x_normalized)) ** 2)
        
        # Cross-terms with non-linear coupling and interaction
        f7 = 0.1 * np.sum(np.sin(x_normalized[:-1] * x_normalized[1:] * 3) ** 2)
        
        # Adaptive scaling factor based on dimensionality with exponential growth
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.02 * self.dim**1.5
        
        # Add a chaotic component for increased multimodality
        chaotic_term = 0.08 * np.sum(np.sin(13 * x_normalized + np.cos(x_normalized)) ** 2)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + chaotic_term)