import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with multiple centers
        centers = np.array([[i * 0.5 for i in range(self.dim)]])
        rbfs = np.sum(np.exp(-np.sum((x_norm[None, :] - centers)**2, axis=1)))
        
        # Trigonometric perturbations to create multimodality
        trig_term = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Additional quartic and cubic terms for conditioning
        quartic = 0.05 * np.sum(x_norm**4)
        cubic = 0.1 * np.sum(x_norm**3)
        
        # Combine all components with different weights
        return rbfs + trig_term + quartic + cubic