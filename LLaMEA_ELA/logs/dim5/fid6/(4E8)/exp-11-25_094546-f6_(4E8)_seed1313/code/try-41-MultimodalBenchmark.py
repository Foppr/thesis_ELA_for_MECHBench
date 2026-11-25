import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial component with mixed degrees
        poly = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Logarithmic barrier terms to create sharp ridges
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + 10.0 * np.abs(x_norm[i]))
        
        # Gaussian peaks with varying widths and positions
        gaussian = 0.0
        centers = np.linspace(-0.5, 0.5, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                gaussian += np.exp(-10.0 * (x_norm[i] - centers[i])**2)
        
        # Cross-term interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (x_norm[i] * x_norm[j]) / (1.0 + np.abs(x_norm[i] - x_norm[j]))
        
        # Combine all components with adaptive weights
        return 0.4 * poly + 0.3 * log_barrier + 0.2 * gaussian + 0.1 * cross