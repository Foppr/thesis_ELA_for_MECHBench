import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian radial basis components with random centers and varying widths
        centers = np.random.uniform(-1, 1, (10, self.dim))
        widths = np.random.uniform(0.1, 2.0, 10)
        gaussian = 0.0
        for i in range(10):
            gaussian += np.exp(-np.sum(widths[i] * (x_scaled - centers[i])**2))
        
        # Trigonometric perturbation with varying frequencies and amplitudes
        trig = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) * np.sin(8 * x_scaled))
        
        # Adaptive conditioning: modify based on dimensionality
        conditioning = np.sum(x_scaled**2) * (1.0 + 0.1 * self.dim)
        
        # Cross-dimensional coupling through polynomial interactions
        coupling = np.sum((x_scaled[:-1] + x_scaled[1:])**4)
        
        # Combine all components with different weights
        return 0.3 * gaussian + 1.2 * trig + 0.8 * conditioning + 0.5 * coupling