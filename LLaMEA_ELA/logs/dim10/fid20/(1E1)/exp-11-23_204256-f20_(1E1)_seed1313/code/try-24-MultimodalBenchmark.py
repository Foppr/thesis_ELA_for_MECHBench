import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Highly chaotic sinusoidal perturbations with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(13 * np.pi * x_normalized + np.sin(5 * x_normalized)) ** 2)
        f3 = 0.25 * np.sum(np.sin(17 * np.pi * x_normalized + np.cos(7 * x_normalized)) ** 2)
        
        # Asymmetric cubic and higher-order polynomial terms
        f4 = 0.1 * np.sum(np.where(x_normalized > 0, x_normalized**3, -0.5 * x_normalized**3))
        f5 = 0.05 * np.sum(np.where(x_normalized > 0, x_normalized**4, -0.3 * x_normalized**4))
        
        # Non-linear cross-terms with exponential interactions
        f6 = 0.15 * np.sum(np.exp(2 * np.abs(x_normalized[:-1] * x_normalized[1:])) - 1)
        
        # Modified interaction terms with sinusoidal modulation
        f7 = 0.1 * np.sum(np.sin(np.pi * x_normalized[:-1] * x_normalized[1:]) ** 2)
        
        # Additional chaotic term with dynamic frequency modulation
        f8 = 0.08 * np.sum(np.sin(9 * np.pi * x_normalized + 0.5 * np.sin(11 * x_normalized)) ** 3)
        
        # Adaptive scaling factor based on dimensionality and chaos level
        adaptive_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.std(x_normalized)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)