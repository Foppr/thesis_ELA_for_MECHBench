import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        f1 = np.sum(x**4 - 2*x**2 + 1)
        
        # Trigonometric component with multiple frequencies
        f2 = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Radial basis function component with varying centers
        centers = np.linspace(-4.0, 4.0, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2))
        
        # Coupled oscillatory terms between dimensions
        f4 = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # High-frequency chaotic-like component
        f5 = np.sum(np.sin(10.0 * x) * np.cos(15.0 * x) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction with exponential decay
        f6 = np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * np.sin(3.0 * (x[:-1] + x[1:])))
        
        # Combined function with adaptive weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.05 * f6