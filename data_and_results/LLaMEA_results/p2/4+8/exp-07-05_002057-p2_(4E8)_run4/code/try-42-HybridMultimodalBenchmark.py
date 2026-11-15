import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbation component with logistic map modulation
        sinusoidal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation using logistic map
            chaotic_factor = np.sin(10 * xi) * np.cos(7 * xi) + 0.7 * np.sin(13 * xi) * np.cos(17 * xi)
            sinusoidal_sum += chaotic_factor * (1 + 0.5 * np.sin(23 * xi) * np.cos(31 * xi))
        
        # Logarithmic conditioning component
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + 0.1 * np.abs(xi)) * np.sin(5 * xi)
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.4 * gaussian_sum + 0.35 * sinusoidal_sum + 0.15 * log_conditioning + 0.1 * quadratic_term
        
        return result