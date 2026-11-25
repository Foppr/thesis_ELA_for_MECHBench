import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(0.5 * x))
        
        # Polynomial potential with mixed exponents
        poly_term = np.sum(0.5 * x**6 + 0.3 * x**4 - 0.8 * x**3 + 1.2 * x**2 - 0.5 * x + 0.9)
        
        # Radial basis function component with Gaussian kernels
        rbf_term = np.sum(np.exp(-0.1 * np.sum((x[:, None] - x[None, :])**2, axis=0)))
        
        # Cross-term interaction between dimensions
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(2.0 * x[:-1] + 0.5 * x[1:]))
        
        # High-frequency chaotic modulation
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.7 * x))) * np.cos(np.exp(np.cos(1.9 * x))))
        
        # Asymmetric barrier function
        barrier_term = np.sum(1.0 / (1.0 + np.exp(-5.0 * (x - 1.0))) + 1.0 / (1.0 + np.exp(5.0 * (x + 1.0))))
        
        # Combine all terms with different weights
        return 0.25 * sin_term + 0.20 * poly_term + 0.15 * rbf_term + 0.12 * cross_term + 0.18 * chaotic_term + 0.08 * barrier_term + 2.0