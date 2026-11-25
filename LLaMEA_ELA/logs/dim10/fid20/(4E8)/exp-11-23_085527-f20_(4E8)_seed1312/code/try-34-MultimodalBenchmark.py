import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6)
        
        # Trigonometric components with multiple frequencies
        f2 = 15 * np.sum(np.sin(8 * x_scaled)**2 + np.cos(6 * x_scaled)**2)
        
        # Exponential terms creating steep gradients
        f3 = 2 * np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        # Cross-terms with non-separable structure
        f4 = 0.8 * np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**2)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # Combined function with adaptive scaling
        return condition_factor * (f1 + f2 + f3 + f4)