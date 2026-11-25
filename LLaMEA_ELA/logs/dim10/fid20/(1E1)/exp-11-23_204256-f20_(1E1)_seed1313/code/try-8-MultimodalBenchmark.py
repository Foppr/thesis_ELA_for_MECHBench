import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # Exponentially scaled sinusoidal perturbations with varying frequencies
        f2 = 0.3 * np.sum(np.exp(5 * np.abs(x_normalized)) * np.sin(9 * np.pi * x_normalized)**2)
        
        # Cross-terms creating complex interaction between dimensions
        f3 = 0.1 * np.sum((x_normalized[:-1] + x_normalized[1:])**2)
        
        # A novel global minimum attraction term with energy-like behavior
        f4 = 0.05 * np.sum(1 / (1 + np.exp(-10 * (np.abs(x_normalized) - 0.5))))
        
        # High-order polynomial for increased complexity
        f5 = 0.03 * np.sum(np.abs(x_normalized)**6)
        
        return f1 + f2 + f3 + f4 + f5