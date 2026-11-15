import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with varying widths and centers
        gaussian_term = np.sum(np.exp(-np.sum((x[:, np.newaxis] - np.linspace(-5, 5, 10))**2, axis=0) / 2.0))
        
        # Sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) + 
                         np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x) + 
                         np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Polynomial coupling with mixed degrees and interaction terms
        poly_coupling = np.sum(0.1 * x**8 + 0.3 * x**6 - 0.5 * x**4 + 0.7 * x**2 - 0.2 * x)
        
        # Cross-dimensional interaction with dynamic scaling and phase shifts
        cross_term = np.sum((x[:-1] * x[1:]) * np.sin(3 * np.pi * (x[:-1] + x[1:])))
        
        # Additional chaotic component with logistic map-like behavior
        chaotic_term = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(4 * np.pi * x))
        
        # Combine all terms with different weights and add offset
        return 0.3 * gaussian_term + 0.25 * sin_term + 0.15 * poly_coupling + 0.1 * cross_term + 0.05 * chaotic_term + 2.0