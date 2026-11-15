import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(2 * np.pi * x * np.exp(-0.1 * x**2)) * np.cos(3 * np.pi * x * np.exp(-0.05 * x**2)))
        
        # Polynomial chaos with mixed monomials and nonlinear interactions
        poly_chaos = np.sum(0.5 * x**8 - 4 * x**6 + 7 * x**4 - 5 * x**2 + 0.5 * x)
        
        # Radial basis function with multiple centers and varying widths
        centers = np.linspace(-5, 5, min(5, self.dim))
        rbfs = np.sum(np.exp(-np.sum((x[:, np.newaxis] - centers)**2, axis=0) / (2 * 0.5**2)))
        
        # Cross-dimensional coupling with trigonometric and exponential interactions
        coupling = np.sum(np.sin(np.pi * (x[:-1] + x[1:])) * np.exp(-0.5 * (x[:-1] - x[1:])**2))
        
        # Multi-scale oscillatory component with varying periods
        multi_scale = np.sum(np.sin(10 * np.pi * x) * np.cos(15 * np.pi * x) * np.sin(5 * np.pi * x))
        
        # Combined function with adaptive weights and global offset
        return 0.3 * chaotic_wave + 0.15 * poly_chaos + 0.25 * rbfs + 0.2 * coupling + 0.1 * multi_scale + 2.1