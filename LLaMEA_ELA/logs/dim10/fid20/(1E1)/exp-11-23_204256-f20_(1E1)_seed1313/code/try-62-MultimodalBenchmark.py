import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Sinusoidal perturbations with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(8 * x_normalized) ** 2)
        f3 = 0.2 * np.sum(np.cos(7 * x_normalized) ** 2)
        f4 = 0.15 * np.sum(np.sin(12 * x_normalized) ** 2)
        
        # Exponential and polynomial interactions
        f5 = 0.1 * np.sum(np.exp(2 * np.abs(x_normalized)) - 1)
        f6 = 0.08 * np.sum(x_normalized**4)
        
        # Asymmetric cross-terms that create rugged landscape
        f7 = 0.1 * np.sum(x_normalized[:-1] ** 3 * x_normalized[1:])
        f8 = 0.05 * np.sum(x_normalized[:-2] ** 2 * x_normalized[1:-1] * x_normalized[2:] ** 3)
        
        # Mixed trigonometric and polynomial interactions
        f9 = 0.07 * np.sum(np.sin(5 * x_normalized) * x_normalized**2)
        f10 = 0.06 * np.sum(np.cos(4 * x_normalized) * x_normalized**3)
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)