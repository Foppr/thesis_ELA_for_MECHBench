import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial interaction terms
        f1 = np.sum(x_scaled**4)
        
        # Sinusoidal modulations with exponential decay
        f2 = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled))
        
        # Cross-terms creating complex interactions
        f3 = np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Additional high-frequency oscillations
        f4 = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled))
        
        # Combined function with varying curvature and multiple local minima
        return 2.0 * f1 + 0.5 * f2 + 0.3 * f3 + 0.1 * f4 + np.sum(np.exp(-x_scaled**2))