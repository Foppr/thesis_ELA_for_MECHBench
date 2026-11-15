import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x_norm[i]**4 - 2*x_norm[i]**2 + 1) * np.sin(x_norm[i] * np.pi)
        
        # Radial basis function with multiple centers
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0.0
            rbf += np.exp(-5 * (x_norm[i] - center)**2)
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x_norm[i] * x_norm[j]) * (1 + 0.1 * (i + j))
        
        # Sine-wave interference pattern
        interference = 0.0
        for i in range(self.dim):
            interference += np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i])
        
        # Global shaping term with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        shaping = np.exp(-r**3) * np.sin(10 * r)
        
        # Combine all components with weighted sum
        return 0.3 * poly_chaos + 0.25 * rbf + 0.2 * coupling + 0.15 * interference + 0.1 * shaping + 1.0