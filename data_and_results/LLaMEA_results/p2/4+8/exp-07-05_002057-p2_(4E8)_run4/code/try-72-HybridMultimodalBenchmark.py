import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (8, dim))
        self.weights = np.random.uniform(0.3, 1.5, 8)
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay RBF component
        rbf_sum = 0.0
        for i in range(8):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rbf_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Trigonometric coupling component
        trig_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            trig_sum += np.sin(3 * xi) * np.cos(5 * xi) * np.sin(7 * xi) + \
                       0.7 * np.cos(4 * xi) * np.sin(6 * xi) * np.cos(8 * xi) + \
                       0.4 * np.sin(2 * xi) * np.cos(9 * xi) * np.sin(11 * xi)
        
        # Adaptive conditioning term
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            adaptive_conditioning += self.conditioning_factors[i] * np.log(1 + xi**2) * np.cos(xi)
        
        # Cubic basin component
        cubic_term = np.sum(x**3) / self.dim
        
        # Combine all components with different weights
        result = 0.35 * rbf_sum + 0.3 * trig_sum + 0.25 * adaptive_conditioning + 0.1 * cubic_term
        
        return result