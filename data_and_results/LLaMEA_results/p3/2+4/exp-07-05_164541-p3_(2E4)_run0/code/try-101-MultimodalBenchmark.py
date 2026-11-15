import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-5, 5, 10)
        widths = np.logspace(-1, 1, 10)
        rbf_sum = 0.0
        for i in range(10):
            rbf_sum += np.exp(-np.sum((x - centers[i])**2) / (2 * widths[i]**2))
        
        # Sinusoidal oscillations with adaptive frequencies and amplitudes
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(2 * np.pi * (i + 1) * x[i]) * np.cos(3 * np.pi * (i + 1) * x[i])
        
        # Adaptive polynomial coupling with dimension-dependent exponents
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += (x[i]**(2 * (i % 4) + 3)) * np.sin(5 * np.pi * x[i])
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross_sum = 0.0
        for i in range(self.dim - 1):
            cross_sum += (x[i] * x[i+1]) * np.sin(4 * np.pi * (x[i] + x[i+1]))
        
        # Combined landscape with dynamic scaling and global offset
        return 0.5 * rbf_sum + 0.3 * sin_sum + 0.2 * poly_sum + 0.1 * cross_sum + 1.5