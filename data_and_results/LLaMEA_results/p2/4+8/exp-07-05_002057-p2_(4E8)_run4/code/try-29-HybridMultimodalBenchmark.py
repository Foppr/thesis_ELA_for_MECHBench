import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Sinusoidal perturbation component
        sinusoidal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            sinusoidal_sum += (np.sin(5 * xi) * np.cos(3 * xi) + 
                              0.5 * np.sin(7 * xi) * np.cos(11 * xi) + 
                              0.3 * np.sin(2 * xi) * np.cos(9 * xi))
        
        # Quadratic basin component
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.5 * gaussian_sum + 0.3 * sinusoidal_sum + 0.2 * quadratic_term
        
        return result