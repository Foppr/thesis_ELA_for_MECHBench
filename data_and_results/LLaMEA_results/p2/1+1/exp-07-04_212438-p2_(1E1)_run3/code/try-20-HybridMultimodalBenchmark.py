import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees and non-separability
        f1 = np.sum(x**6 - 3*x**4 + 3*x**2 - 1)
        
        # Trigonometric component with varying frequencies and phase shifts
        f2 = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x) * np.sin(7.0 * x) * np.cos(9.0 * x))
        
        # Radial basis function with adaptive centers and varying widths
        centers = np.linspace(-4.5, 4.5, self.dim)
        widths = np.linspace(0.5, 2.0, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths))
        
        # Coupled oscillatory terms with dynamic coupling strength
        f4 = np.sum(np.sin(2.0 * x[:-1] * x[1:]) * np.cos(2.0 * (x[:-1] + x[1:])))
        
        # High-frequency chaotic-like component with feedback
        f5 = np.sum(np.sin(15.0 * x) * np.cos(20.0 * x) * np.exp(-0.05 * x**2) * np.sin(0.5 * np.sum(x**2)))
        
        # Cross-term interaction with exponential decay and sinusoidal modulation
        f6 = np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * np.sin(5.0 * (x[:-1] + x[1:])) * np.cos(2.0 * x[:-1]))
        
        # Additional non-separable component with mixed interactions
        f7 = np.sum((x[:-1] + x[1:])**2 * np.sin(3.0 * x[:-1]) * np.cos(3.0 * x[1:]))
        
        # Combined function with adaptive weights and normalization
        return 0.4 * f1 + 0.25 * f2 + 0.15 * f3 + 0.12 * f4 + 0.08 * f5 + 0.07 * f6 + 0.03 * f7