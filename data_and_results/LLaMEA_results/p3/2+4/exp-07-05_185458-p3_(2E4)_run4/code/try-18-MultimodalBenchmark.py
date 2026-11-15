import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        f2 = np.sum(np.sin(15 * np.pi * x_norm + np.sin(7 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1)) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms for non-convexity and varied curvature
        f4 = np.sum(x_norm**4 + 0.3 * x_norm**6 + 0.1 * x_norm**8)
        
        # Cross-terms with trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.sin(x_norm[:-1] * x_norm[1:] * np.sin(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns
        f6 = np.sum(np.sin(5 * np.pi * x_norm * np.sin(3 * np.pi * x_norm)) ** 2)
        
        # Higher-order trigonometric coupling for increased complexity
        f7 = np.sum(np.sin(10 * np.pi * x_norm * np.sin(5 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm)) ** 2)
        
        # Adaptive difficulty based on dimensionality
        f8 = np.sum(np.sin(np.pi * x_norm * np.sin(2 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm)) ** 2)
        
        # Combine all terms with varying weights
        return f1 + 0.7 * f2 + 0.4 * f3 + 0.08 * f4 + 0.3 * f5 + 0.15 * f6 + 0.2 * f7 + 0.1 * f8