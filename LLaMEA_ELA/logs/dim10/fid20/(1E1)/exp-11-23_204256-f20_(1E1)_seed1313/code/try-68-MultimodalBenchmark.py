import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic sinusoidal perturbations with non-linear frequency modulation
        f2 = 0.6 * np.sum(np.sin(12 * np.pi * x_normalized + np.sin(7 * x_normalized)) ** 2)
        f3 = 0.4 * np.sum(np.sin(18 * np.pi * x_normalized + np.cos(5 * x_normalized)) ** 2)
        
        # Higher-order polynomial terms with alternating signs for increased complexity
        f4 = 0.12 * np.sum(x_normalized**3)
        f5 = 0.09 * np.sum(x_normalized**4)
        f6 = 0.06 * np.sum(x_normalized**6)
        
        # Exponential modulation of trigonometric terms for dynamic difficulty
        f7 = 0.2 * np.sum(np.exp(2 * np.abs(x_normalized)) * np.sin(8 * np.pi * x_normalized) ** 2)
        
        # Novel cross-dimensional coupling with chaotic interaction coefficients
        f8 = 0.15 * np.sum(x_normalized[:-1] ** 3 * x_normalized[1:] ** 2)
        f9 = 0.10 * np.sum(x_normalized[:-2] ** 2 * x_normalized[1:-1] * x_normalized[2:] ** 3)
        
        # Adaptive exponential scaling factor based on dimensionality and chaos
        adaptive_scale = 1.0 + 0.35 * np.exp(0.08 * self.dim) * (1.0 + 0.1 * np.sum(np.sin(x_normalized)**2))
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)