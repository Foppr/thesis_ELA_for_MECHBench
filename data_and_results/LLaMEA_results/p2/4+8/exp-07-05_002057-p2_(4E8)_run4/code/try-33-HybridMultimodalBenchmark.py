import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.3, 2.5, 10)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.4 ** 2))
        
        # Sinusoidal perturbation component with modified frequencies
        sinusoidal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            sinusoidal_sum += (0.8 * np.sin(7 * xi) * np.cos(5 * xi) + 
                              0.6 * np.sin(9 * xi) * np.cos(13 * xi) + 
                              0.4 * np.sin(3 * xi) * np.cos(11 * xi))
        
        # Add cross-term interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x[i]) * np.cos(x[j])
        
        # Quadratic basin component
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.4 * gaussian_sum + 0.3 * sinusoidal_sum + 0.2 * cross_term + 0.1 * quadratic_term
        
        return result