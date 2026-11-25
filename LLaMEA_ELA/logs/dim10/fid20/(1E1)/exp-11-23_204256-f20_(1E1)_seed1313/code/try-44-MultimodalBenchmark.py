import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency trigonometric terms with varying amplitudes
        f2 = 0.3 * np.sum(np.sin(10 * x_norm) ** 2)
        f3 = 0.2 * np.sum(np.cos(15 * x_norm) ** 2)
        
        # Exponential scaling based on dimensionality and input values
        exp_term = np.exp(0.1 * np.sum(np.abs(x_norm)))
        f4 = 0.15 * exp_term
        
        # Asymmetric cross-terms that create complex interactions
        cross1 = np.sum(x_norm[:-1] ** 3 * x_norm[1:])
        cross2 = np.sum(x_norm[:-2] ** 2 * x_norm[1:-1] * x_norm[2:])
        f5 = 0.1 * (cross1 + cross2)
        
        # Polynomial terms with different degrees
        f6 = 0.05 * np.sum(x_norm**4)
        f7 = 0.02 * np.sum(x_norm**6)
        
        # Additional periodic term with phase shift
        f8 = 0.1 * np.sum(np.sin(7 * np.pi * x_norm + np.pi/4) ** 2)
        
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)