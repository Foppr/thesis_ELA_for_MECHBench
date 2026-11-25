import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Exponential decay terms with varying rates
        f2 = 0.2 * np.sum(np.exp(-x_norm**2 / 2.0))
        
        # Sine wave periodic components with different frequencies and phases
        f3 = 0.15 * np.sum(np.sin(5 * x_norm + np.pi/4)**2)
        f4 = 0.1 * np.sum(np.sin(9 * x_norm - np.pi/3)**2)
        
        # Asymmetric cross-terms that create non-separable interactions
        f5 = 0.08 * np.sum(x_norm[:-1] * np.exp(-x_norm[1:]**2))
        
        # Cubic and quartic terms for additional curvature
        f6 = 0.03 * np.sum(x_norm**3)
        f7 = 0.02 * np.sum(x_norm**4)
        
        # Combined effect with adaptive scaling based on dimensionality
        adaptive_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return adaptive_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7)