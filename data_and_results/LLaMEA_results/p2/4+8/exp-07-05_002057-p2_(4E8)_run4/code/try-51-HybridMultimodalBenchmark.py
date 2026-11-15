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
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbation component with modified frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (0.8 * np.sin(7 * xi) * np.cos(4 * xi) * np.sin(9 * xi) + 
                           0.6 * np.sin(13 * xi) * np.cos(3 * xi) * np.sin(11 * xi) + 
                           0.4 * np.sin(5 * xi) * np.cos(7 * xi) * np.sin(10 * xi))
        
        # Logarithmic conditioning term with cross-dimensional interaction
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * np.sin(xi)
        
        # Cross-dimensional polynomial interaction term
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * x[i] * x[j] * np.sin(x[i] + x[j])
        
        # Quadratic basin component
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.35 * gaussian_sum + 0.3 * chaotic_sum + 0.2 * log_conditioning + 0.1 * cross_term + 0.05 * quadratic_term
        
        return result