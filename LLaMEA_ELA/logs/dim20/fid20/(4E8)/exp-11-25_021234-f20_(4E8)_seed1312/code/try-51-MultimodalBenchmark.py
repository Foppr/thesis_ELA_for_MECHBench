import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # Periodic exponential decay modulations with varying rates
        f2 = 0.5 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(2.0 * np.pi * x))
        
        # Asymmetric saddle points with directional bias
        f3 = 0.3 * np.sum((x**2) * np.cos(3.0 * x) * np.sin(1.5 * x))
        
        # Adaptive ridge structures that change with dimensionality
        f4 = 0.2 * np.sum(np.sin(4.0 * x) * np.exp(-0.1 * np.abs(x)) * (1.0 + 0.1 * self.dim * np.cos(2.0 * x)))
        
        # Multi-scale fractal-like peaks using nested sinusoids
        f5 = 0.15 * np.sum(np.sin(8.0 * x) * np.sin(4.0 * x) * np.exp(-0.05 * x**2))
        
        # Non-smooth regions via fractional powers with adaptive exponents
        f6 = 0.1 * np.sum(np.abs(x)**(1.3 + 0.05 * np.sin(self.dim)))
        
        return f1 + f2 + f3 + f4 + f5 + f6