import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Trigonometric terms creating oscillations with modified frequencies
        f2 = np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Exponential terms creating steep gradients
        f3 = np.sum(np.exp(-2 * x_scaled**2) - 1)
        
        # Cross-terms creating interaction between dimensions with sine modulation
        f4 = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(2 * np.pi * x_scaled[:-1]))
        
        # Additional exponential cross-term interaction
        f5 = np.sum(np.exp(-x_scaled[:-1]**2 - x_scaled[1:]**2) * x_scaled[:-1] * x_scaled[1:])
        
        # Combine all terms with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.1 * f5