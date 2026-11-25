import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion terms with varying degrees
        poly_term = np.sum((x**4 + 0.5 * x**3 - 0.3 * x**2 + 0.1 * x) * np.exp(-0.1 * x**2))
        
        # Sinusoidal coupling with adaptive frequencies based on dimension
        freqs = np.arange(1, self.dim + 1)
        sin_coupling = np.sum(np.sin(freqs * x) * np.cos(freqs * x) * np.exp(-0.05 * x**2))
        
        # Radial basis function with adaptive scaling and multi-scale interactions
        r_squared = np.sum(x**2)
        rbf_term = np.sum(np.exp(-0.2 * (x - np.sin(x))**2) * np.log(1 + 0.1 * r_squared))
        
        # High-dimensional interference pattern with cross-dimensional coupling
        interference = np.sum(np.sin(0.5 * x[:-1] + 0.3 * x[1:]) * np.cos(0.4 * x[:-1] - 0.2 * x[1:]))
        
        # Combined function with dynamic weights
        return 0.4 * poly_term + 0.3 * sin_coupling + 0.2 * rbf_term + 0.1 * interference