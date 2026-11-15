import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees and chaotic coefficients
        f1 = np.sum(0.7 * x_scaled**6 + 0.4 * x_scaled**5 + 0.2 * x_scaled**4 + 0.1 * x_scaled**3)
        
        # Trigonometric terms with chaotic frequencies and phase shifts
        f2 = np.sum(np.sin(5 * np.pi * x_scaled + np.sin(3 * x_scaled)) * np.cos(4 * np.pi * x_scaled + np.cos(2 * x_scaled)))
        
        # Exponential terms with radial barriers and steep gradients
        f3 = np.sum(np.exp(-2 * x_scaled**2) - np.exp(-0.5 * x_scaled**2) + 0.5 * np.exp(-x_scaled**4))
        
        # Cross-terms with non-linear coupling and interaction
        f4 = np.sum(np.sin(np.pi * x_scaled[:-1] * x_scaled[1:]) * np.cos(np.pi * x_scaled[:-1] + x_scaled[1:]))
        
        # Additional chaotic cross-dimensional interaction
        f5 = np.sum(np.sin(np.pi * np.sum(x_scaled**2)) * np.cos(np.pi * np.sum(x_scaled**3)))
        
        # Combine all terms with different weights
        return 0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.08 * f4 + 0.02 * f5