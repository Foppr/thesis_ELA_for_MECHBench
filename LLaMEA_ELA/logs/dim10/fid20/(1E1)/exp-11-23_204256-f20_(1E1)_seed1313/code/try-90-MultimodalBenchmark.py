import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic sinusoidal perturbations with prime frequencies and varying amplitudes
        f2 = 0.7 * np.sum(np.sin(13 * np.pi * x_normalized) ** 2)
        f3 = 0.5 * np.sum(np.sin(19 * np.pi * x_normalized) ** 2)
        f4 = 0.4 * np.sum(np.sin(23 * np.pi * x_normalized) ** 2)
        
        # Higher-order polynomial terms with non-uniform exponents
        f5 = 0.2 * np.sum(x_normalized**4)
        f6 = 0.15 * np.sum(x_normalized**6)
        f7 = 0.1 * np.sum(np.abs(x_normalized)**3.5)
        
        # Complex cross-terms with non-linear interaction patterns
        f8 = 0.2 * np.sum(x_normalized[:-1] ** 4 * x_normalized[1:] ** 2)
        f9 = 0.18 * np.sum(x_normalized[:-2] ** 3 * x_normalized[1:-1] ** 5 * x_normalized[2:] ** 2)
        f10 = 0.12 * np.sum(x_normalized[:-3] ** 2 * x_normalized[1:-2] ** 4 * x_normalized[2:-1] ** 3 * x_normalized[3:] ** 2)
        
        # Exponential conditioning factor with chaotic scaling based on dimensionality
        adaptive_scale = 1.0 + 0.5 * np.exp(0.1 * self.dim) + 0.2 * np.sin(0.05 * self.dim * np.pi)
        
        # Add a chaotic perturbation term based on the sum of all dimensions
        chaos_term = 0.3 * np.sin(np.sum(x_normalized) * 50)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10) + chaos_term