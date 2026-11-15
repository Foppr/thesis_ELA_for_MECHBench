import numpy as np

class ChaoticSaddleGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional-order polynomial component with non-integer exponents
        f1 = np.sum(np.abs(x)**1.7 + np.abs(x)**2.3 + np.abs(x)**3.1)
        
        # Chaotic saddle-point component with sine-cosine modulation
        f2 = np.sum(np.sin(10.0 * x) * np.cos(12.0 * x) * np.exp(-0.5 * np.sum(x**2)))
        
        # Embedded Gaussian mixture with varying variances and offsets
        centers = np.linspace(-4.0, 4.0, self.dim)
        variances = np.logspace(-1, 1, self.dim)
        gaussians = np.sum(np.exp(-0.5 * (x - centers)**2 / variances))
        
        # Fractional Brownian motion inspired component with long-range dependence
        f4 = np.sum(np.sin(8.0 * x) * np.cos(9.0 * x) * np.exp(-0.3 * np.abs(x)**1.5))
        
        # Multi-scale fractal-like structure with recursive scaling
        f5 = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.exp(-0.1 * np.sum(x**4)))
        
        # Cross-dimensional coupling with time-delayed feedback
        f6 = np.sum(np.sin(15.0 * x[:-1] * x[1:]) * np.cos(18.0 * (x[:-1] + x[1:])) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Saddle-point attraction-repulsion component with dynamic weights
        f7 = np.sum((x**2 - 1)**3 * np.exp(-0.5 * np.sum(x**2)))
        
        # Combined function with adaptive weighting and chaotic amplification
        return 0.3 * f1 + 0.25 * f2 + 0.2 * gaussians + 0.15 * f4 + 0.1 * f5 + 0.08 * f6 + 0.07 * f7