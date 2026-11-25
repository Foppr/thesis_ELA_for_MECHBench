import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base term with mixed degrees
        f1 = np.sum(x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2)
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rb_f = 0
        for i in range(min(5, self.dim)):
            rb_f += np.exp(-10 * np.sum((x_norm - centers[i])**2))
        
        # High-frequency trigonometric oscillations
        f3 = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm))
        
        # Coupled sine waves with varying amplitudes
        f4 = np.sum(np.sin(8 * x_norm) * np.sin(12 * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Interaction term with Gaussian-like decay
        f5 = np.sum(np.exp(-0.5 * np.sum((x_norm[:, None] - x_norm[None, :])**2, axis=0)) * 
                   np.sin(3 * np.pi * x_norm))
        
        # Weighted combination with dimensionality-dependent scaling
        scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale * (0.4 * f1 + 0.25 * rb_f + 0.2 * f3 - 0.1 * f4 + 0.05 * f5) + 0.01 * np.sum(np.abs(x_norm)**3)